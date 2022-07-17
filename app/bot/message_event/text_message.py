# 3rd
from linebot.models import (
    TextSendMessage, )

# our
from ..common import line_bot_api
from app.recommend.recommender import get_daily_recommended_phrases


def text_message_dispatcher(event):
    '''
        @params:
            event: Line request event
    '''
    reply_token = event.reply_token
    supported_commands = {
        'help': show_help_message,
        'rc': show_recommended_phrases
    }
    reply_text = ''
    if event.message.text in supported_commands:
        reply_text = supported_commands[event.message.text]()
    else:
        reply_text = '測試不回話'

    reply_text_message(reply_token, reply_text)


def reply_text_message(reply_token, reply_text=''):
    '''
        @params:
            reply_token: Line reply token
            reply_text: Text message we want to send back to user
    '''
    line_bot_api.reply_message(reply_token, TextSendMessage(text=reply_text))


def show_help_message():
    ''' Show the help message when user types 'help'
    '''
    text = '''輸入下列任一指令取得幫助:
    * help: 顯示此訊息
    * rc: 顯示今日推薦的片語
    '''
    return text


def show_recommended_phrases():
    ''' Show the pharses when user types 'rc'
    '''
    text = get_daily_recommended_phrases()
    return text
