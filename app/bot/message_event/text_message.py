# 3rd
from linebot.models import (
    TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageAction, URIAction)

# our
from ..common import line_bot_api
from app.recommend.recommender import get_daily_recommended_phrases


def text_message_dispatcher(event):
    '''
        @params:
            event: Line request event
    '''

    carousel_template_message = TemplateSendMessage(
             alt_text='免費教學影片',
             template=CarouselTemplate(
                 columns=[
                     CarouselColumn(
                         thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                         title='Python基礎教學',
                         text='萬丈高樓平地起',
                         actions=[
                             MessageAction(
                                 label='教學內容',
                                 text='拆解步驟詳細介紹安裝並使用Anaconda、Python、Spyder、VScode…'
                             ),
                             URIAction(
                                 label='馬上查看',
                                 uri='https://marketingliveincode.com/?page_id=270'
                             )
                         ]
                     ),
                     CarouselColumn(
                         thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
                         title='Line Bot聊天機器人',
                         text='台灣最廣泛使用的通訊軟體',
                         actions=[
                             MessageAction(
                                 label='教學內容',
                                 text='Line Bot申請與串接'
                             ),
                             URIAction(
                                 label='馬上查看',
                                 uri='https://marketingliveincode.com/?page_id=2532'
                             )
                         ]
                     ),
                     CarouselColumn(
                         thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                         title='Telegram Bot聊天機器人',
                         text='唯有真正的方便，能帶來意想不到的價值',
                         actions=[
                             MessageAction(
                                 label='教學內容',
                                 text='Telegrame申請與串接'
                             ),
                             URIAction(
                                 label='馬上查看',
                                 uri='https://marketingliveincode.com/?page_id=2648'
                             )
                         ]
                     )
                 ]
             )
    )

    reply_token = event.reply_token
    supported_commands = {
        'help': show_help_message,
        'rc': show_recommended_phrases
    }
    reply_text = ''
    if event.message.text in supported_commands:
        reply_text = supported_commands[event.message.text]()
        reply_text_message(reply_token, reply_text)
    elif event.message.text == 'test':
        line_bot_api.reply_message(reply_token, carousel_template_message)
    else:
        reply_text = '測試不回話'
        reply_text_message(reply_token, reply_text)

    # reply_text_message(reply_token, reply_text)


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
