import os
import sys
from argparse import ArgumentParser

# 3rd
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookParser)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
)

# our
from src.cache.cache import cache, cache_config
from src.db.db import init_db

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

app = Flask(__name__)
# Init cache
cache.init_app(app, config=cache_config)
# Init db
init_db()


@app.route('/')
def index():
    return 'success佈署!!'


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

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

        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=event.message.text))

    return 'OK'


if __name__ == "__main__":
    arg_parser = ArgumentParser(usage='Usage: python ' + __file__ +
                                ' [--port <port>] [--help]')
    arg_parser.add_argument('-p',
                            '--port',
                            type=int,
                            default=8000,
                            help='port')
    arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    options = arg_parser.parse_args()

    app.run(debug=options.debug, port=options.port)
