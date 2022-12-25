import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user", "score", "teams","games","ranking",
        "team_list",
        "team_roster","team_games",
        "game_score",
        "endstate", 
    ],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "score",
            "conditions": "is_going_to_score",
        },
        {
            "trigger": "advance",
            "source": "score",
            "dest": "team_list",
            "conditions": "is_going_to_team_list",
        },
        {
            "trigger": "advance",
            "source": "team_list",
            "dest": "teams",
            "conditions": "is_going_to_teams",
        },
        {
            "trigger": "advance",
            "source": "teams",
            "dest": "team_list",
            "conditions": "is_going_to_back",
        },
        {
            "trigger": "advance",
            "source": "score",
            "dest": "ranking",
            "conditions": "is_going_to_ranking",
        },
        {
            "trigger": "advance",
            "source": "score",
            "dest": "games",
            "conditions": "is_going_to_games",
        },
        {
            "trigger": "advance",
            "source": ["games","game_score","ranking"],
            "dest": "score",
            "conditions": "is_going_to_back",
        },
        {
            "trigger": "advance",
            "source": "teams",
            "dest": "team_roster",
            "conditions": "is_going_to_team_roster",  
        },
        {
            "trigger": "advance",
            "source": "team_roster",
            "dest": "teams",
            "conditions":"is_going_to_back"
        },
        {
            "trigger": "advance",
            "source": "teams",
            "dest": "team_games",
            "conditions": "is_going_to_team_games",
        },
        {
            "trigger": "advance",
            "source": "team_games",
            "dest": "teams",
            "conditions": "is_going_to_back",
        },
        {
            "trigger": "advance",
            "source": "team_games",
            "dest": "games",
            "conditions": "is_going_to_more_games",
        },
        {
            "trigger": "advance",
            "source": ["games","game_score"],
            "dest": "game_score",
            "conditions": "is_going_to_game_score",
        },
        {
            "trigger": "advance",
            "source": ["teams","games",
                "team_games","team_roster",
                "ranking","game_score"],
            "dest": "endstate",
            "conditions": "is_going_to_endstate",
        },
        {"trigger": "go_back", "source":["endstate"], 
         "dest": "user"
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK" 


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        #------------------------------------------------------------
        if response == False:
            if event.message.text.lower() == 'fsm':
                show_fsm()
                #send_image_message(event.reply_token,url)
            elif machine.state == 'user':
                send_text_message(event.reply_token,'type [hi] to start')
            elif machine.state == 'team_list':
                send_text_message(event.reply_token,'invalid team name')
            else:
                send_text_message(event.reply_token, "????")
        
    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
