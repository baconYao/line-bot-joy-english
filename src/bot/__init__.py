import sys
from os import getenv

# 3rd
from flask import Blueprint
from flask import current_app
from flask import request, abort
from linebot.exceptions import (InvalidSignatureError)
from linebot import (LineBotApi, WebhookParser)
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)

# get channel_secret and channel_access_token from your environment variable
channel_secret = getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
line_parser = WebhookParser(channel_secret)

line_bot_bp = Blueprint('line-bot', __name__, url_prefix='/line-bot')


@line_bot_bp.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    current_app.logger.info('Request body: ' + body)
    # parse webhook body
    try:
        events = line_parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=event.message.text))

    return 'OK'
