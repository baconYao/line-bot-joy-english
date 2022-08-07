# 3rd
from linebot.models import (
    TextSendMessage, TemplateSendMessage, CarouselTemplate, CarouselColumn, MessageAction, URIAction)

# our
from ..common import line_bot_api
from app.recommend.recommender import get_daily_recommended_phrases, all_to_daily_cache
from app.cache.cache import cache, CACHE_DAILY_PHRASE


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
        reply_text_message(reply_token, reply_text)
    elif event.message.text == 'test':
        all_to_daily_cache()
        phrases = cache.get(CACHE_DAILY_PHRASE)
        carousel_template_message = TemplateSendMessage(
             alt_text='免費教學影片',
             template=CarouselTemplate(
                 columns=[
                     CarouselColumn(
                         thumbnail_image_url='https://i.imgur.com/wpM584d.jpg',
                         title='每日推薦一',
                         text='字庫編號 : '+str(phrases[0]["id"]),
                         actions=[
                             MessageAction(
                                 label='教學內容',
                                 text=phrases[0]["phrase"]+'\n'+phrases[0]["cn"]
                             ),
                             URIAction(
                                 label='小小測驗',
                                 uri='https://marketingliveincode.com/?page_id=270'
                             )
                         ]
                     ),
                     CarouselColumn(
                         thumbnail_image_url='https://i.imgur.com/W7nI6fg.jpg',
                         title='每日推薦二',
                         text='字庫編號 : '+str(phrases[1]["id"]),
                         actions=[
                             MessageAction(
                                 label='教學內容',
                                 text=phrases[1]["phrase"]+'\n'+phrases[1]["cn"]
                             ),
                             URIAction(
                                 label='小小測驗',
                                 uri='https://marketingliveincode.com/?page_id=2532'
                             )
                         ]
                     ),
                     CarouselColumn(
                         thumbnail_image_url='https://i.imgur.com/l7rzfIK.jpg',
                         title='每日推薦三',
                         text='字庫編號 : '+str(phrases[2]["id"]),
                         actions=[
                             MessageAction(
                                 label='教學內容',
                                 text=phrases[2]["phrase"]+'\n'+phrases[2]["cn"]
                             ),
                             URIAction(
                                 label='小小測驗',
                                 uri='https://marketingliveincode.com/?page_id=2648'
                             )
                         ]
                     )
                 ]
             )
        )
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
