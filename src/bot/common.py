import sys
from os import getenv


from linebot import (LineBotApi, WebhookParser)

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
