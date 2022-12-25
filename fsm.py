from transitions.extensions import GraphMachine
from utils import send_text_message, send_button_message, send_image_message, send_text_button_message
import requests
from linebot.models import MessageTemplateAction
import pandas as pd

flag ={
        'ARG':'\U0001F1E6\U0001F1F7',
        'FRA':'\U0001F1EB\U0001F1F7',
        'CRO':'\U0001F1ED\U0001F1F7',
        'MAR':'\U0001F1F2\U0001F1E6',
        'ENG':'\U0001F3F4\U000E0067\U000E0062\U000E0065\U000E006E\U000E0067\U000E007F',
        'BRA':'\U0001F1E7\U0001F1F7',
        'NED':'\U0001F1F3\U0001F1F1',
        'POR':'\U0001F1F5\U0001F1F9',
        'JPN':'\U0001F1EF\U0001F1F5',
        'KOR':'\U0001F1F0\U0001F1F7',
        'ESP':'\U0001F1EA\U0001F1F8',
        'AUS':'\U0001F1E6\U0001F1FA',
        'USA':'\U0001F1FA\U0001F1F8',
        'SUI':'\U0001F1E8\U0001F1ED',
        'POL':'\U0001F1F5\U0001F1F1',
        'SEN':'\U0001F1F8\U0001F1F3'
    }


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_score(self, event):
        text = event.message.text
        return text.lower() == "hi"

    def is_going_to_team_list(self, event):
        text = event.message.text
        print(text)
        return text.lower() == "teams"
    
    def is_going_to_games(self, event):
        text = event.message.text
        return text.lower() == "games"
    
    def is_going_to_ranking(self, event):
        text = event.message.text
        return text.lower() == "ranking"

    def is_going_to_teams(self, event):
        text = event.message.text
        global team
        team_list = ['fra', 'arg', 'cro', 'mar','eng','por','bra','ned','jpn','usa','kor','sen','sui','aus','esp','pol']
        a = False
        for t in team_list:
            if text.lower() == t:
                a = True
                team = text.lower() 
        return a
    
    def is_going_to_more_games(self,event):
        text = event.message.text
        return text.lower() == "more"

    def is_going_to_team_roster(self, event):
        text = event.message.text
        return text.lower() == "roster"
     
    def is_going_to_team_games(self, event):
        text = event.message.text
        return text.lower() == "games"

    def is_going_to_game_score(self, event):
        text = event.message.text
        global rnd
        rlist = ['2','4','8','16']
        a = False
        for r in rlist:
            if text == r:
                a = True
                rnd = text 
        return a
  
    def is_going_to_endstate(self, event):
        text = event.message.text
        return text.lower() == "bye"

    def is_going_to_back(self, event):
        text = event.message.text
        return text.lower() == "back"

    #========================================================
    def on_enter_score(self, event):
        print("I'm entering score")

        reply_token = event.reply_token
        #send_text_message(reply_token, "Trigger state1")
        btn = [
            MessageTemplateAction(
                label = 'Teams',
                text ='Teams'
            ),
            MessageTemplateAction(
                label = 'Ranking',
                text = 'Ranking'
            ),
            MessageTemplateAction(
                label = 'Game Score',
                text = 'games'
            ),
        ]
        title = 'FIFA WORLD CUP 2022 scoreboard'
        text = 'MENU'
        url = 'https://i.imgur.com/u8DrqhB.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

    #--------------------------------------
    def on_enter_team_list(self, event):
        print("I'm entering Team list")
        reply_token = event.reply_token
        send_text_message(reply_token, "Enter Teams:")

    #---------------------------------------
    def on_enter_games(self, event):
        print("I'm entering games")
        reply_token = event.reply_token
        #send_text_message(reply_token, "Trigger state1")
        btn = [
            MessageTemplateAction(
                label = 'Final',
                text ='2'
            ),
            MessageTemplateAction(
                label = 'SemiFinals',
                text = '4'
            ),
            MessageTemplateAction(
                label = 'QuarterFinal',
                text = '8'
            ),
            MessageTemplateAction(
                label = 'EighthFinal',
                text = '16'
            ),

        ]
        title = 'FIFA WORLD CUP 2022 scoreboard'
        text = 'MENU'
        url = 'https://i.imgur.com/u8DrqhB.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

    #---------------------------------------
    def on_enter_ranking(self, event):
        print("I'm entering ranking")
        reply_token = event.reply_token
        text = '1.' + flag['ARG'] + ' 4W2T1L\n'  
        text += '2.' + flag['FRA'] + ' 5W1T1L\n' 
        text += '3.' + flag['CRO'] + ' 2W4T1L\n'
        text += '4.' + flag['MAR'] + ' 3W2T2L\n'
        text += '5.' + flag['NED'] + ' 3W2T0L\n' 
        text += '6.' + flag['ENG'] + ' 3W1T1L\n'
        text += '7.' + flag['BRA'] + ' 3W1T1L\n' 
        text += '8.' + flag['POR'] + ' 3W0T2L' 
        send_text_message(reply_token, text)
    #--------------------------------------
    def on_enter_teams(self, event):
        print("I'm entering teams")
        global team
        team_img={
                'arg':'https://i.imgur.com/fCEiRVs.png',
                'fra':'https://i.imgur.com/nlO1k7v.png',
                'cro':'https://i.imgur.com/AoCCDoS.jpg',
                'mar':'https://i.imgur.com/YQSWGxh.png',
                'bra':'https://i.imgur.com/JqrphsG.png',
                'ned':'https://i.imgur.com/zy7Zbqh.png',
                'eng':'https://i.imgur.com/tEK8m1s.png',
                'por':'https://i.imgur.com/sDCyeys.png',
                'jpn':'https://i.imgur.com/6gl9rvB.png',
                'usa':'https://i.imgur.com/vqR8R9O.png',
                'sen':'https://i.imgur.com/aNl00Bb.png',
                'pol':'https://i.imgur.com/eyL9JAs.png',
                'kor':'https://i.imgur.com/oUNdY3a.png',
                'aus':'https://i.imgur.com/Vmt6lUi.png',
                'sui':'https://i.imgur.com/fmTQHuj.png',
                'esp':'https://i.imgur.com/erg7V17.png'
                }
        reply_token = event.reply_token
        #send_text_message(reply_token, "Trigger state1")
        btn = [
            MessageTemplateAction(
                label = 'Roster',
                text ='Roster'
            ),
            MessageTemplateAction(
                label = 'Game Score',
                text = 'games'
            ),
            MessageTemplateAction(
                label = 'back',
                text = 'back'
            ),
        ]
        title = '___________'
        text = 'look up for'
        url = team_img[team]
        send_button_message(event.reply_token, title, text, btn, url)

    #----------------------------------------
    def on_enter_team_roster(self, event):
        print("I'm entering roster")
        global team
        t = team.upper() 
        reply_token = event.reply_token
        df = pd.read_csv('./roster.csv')
        df2 = df[(df['team']==t)]
        text = '___________'+t+'____________'
        for index,row in df2.iterrows():
            text +='\n'
            text += row['pos']
            text +=" "
            text += row['name']
            if(row['cap']):
                text+='\U0001F6E1'
        text += '\n\n--->type [back] to see more<---'
        text += '\n->type [bye] if you wanna end<-\n'
        send_text_message(reply_token, text)
    #----------------------------------------
    def on_enter_team_games(self, event):
        print("I'm entering team_games")
        global team
        reply_token = event.reply_token
        text = Show_Team_Score(team)
        send_text_message(reply_token, text)
    #---------------------------------------
    def on_enter_game_score(self, event):
        print("I'm entering game_score")
        reply_token = event.reply_token
        global rnd 
        text1 = Show_Round_Score(rnd)
        btn = [
            MessageTemplateAction(
                label = 'Final',
                text ='2'
            ),
            MessageTemplateAction(
                label = 'SemiFinals',
                text = '4'
            ),
            MessageTemplateAction(
                label = 'QuarterFinal',
                text = '8'
            ),
            MessageTemplateAction(
                label = 'EighthFinal',
                text = '16'
            ),

        ]
        title = 'FIFA WORLD CUP 2022 scoreboard'
        text = 'MENU'
        url = 'https://i.imgur.com/u8DrqhB.jpg'
        send_text_button_message(reply_token, title, text, btn, url, text1)
     #----------------------------------------
    def on_enter_endstate(self,event):
        reply_token = event.reply_token
        text = 'thx for your using, type [hi] if you want to see more..'
        send_text_message(reply_token, text)
        self.go_back()
#===================================================================================        
def Show_Team_Score(t):
    df = pd.read_csv('./gamescore.csv')
    print('------------')
    t = t.upper()
    df2 = df[(df['Win']==t)|(df['Lost']==t)]
    rds = {
            '2':'Final:\n',
            '3':'3rd place match:\n',
            '4':'SemiFinal:\n',
            '8':'QuarterFinal:\n',
            '16':'16 RonudGame:\n'
        }
    text = '_____'+ flag[t]+t+flag[t] + '_____' +'\n' 
    text +="================\n"
    for index, row in df2.iterrows():
        text += rds[str(row['round'])]
        text += row['Win']
        text += flag[row['Win']]
        text += str(row['WinScore'])
        text += ':'
        text += str(row['LoseScore'])
        text += flag[row['Lost']]
        text += row['Lost']
        text += '\n================\n'
    return text
 
def Show_Round_Score(r):
    df = pd.read_csv('./gamescore.csv')
    df2 = df[(df['round']==int(r))]
    rds = {
            '2':'Final:\n',
            '3':'3rd place match:\n',
            '4':'SemiFinal:\n',
            '8':'QuarterFinal:\n',
            '16':'16 RonudGame:\n',
        }
    text = rds[str(r)]
    text +="\n---------------\n"
    for index, row in df2.iterrows():
        text += row['Win']
        text += flag[row['Win']]
        text += str(row['WinScore'])
        text += ':'
        text += str(row['LoseScore'])
        text += flag[row['Lost']]
        text += row['Lost']
        text += '\n-----------------\n'
    return text

