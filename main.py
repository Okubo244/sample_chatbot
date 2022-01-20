import json, webbrowser
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open('info.json', 'r')
info = json.load(file)

url = "https://scraping-for-beginner.herokuapp.com/ranking/"

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text = "こんにちは! \n 本日のランキングサイトです。 \n webbrowser.open(url)")
    line_bot_api.push_message(USER_ID, messages = messages)
    
if __name__ == "__main__":
    main()
