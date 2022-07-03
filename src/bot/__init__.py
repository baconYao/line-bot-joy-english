# 3rd
from flask import Blueprint
from flask import current_app
from flask import request, abort
from linebot.exceptions import (InvalidSignatureError)

# our
from .common import line_parser
from .event_handler import event_broker

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

    event_broker(events)

    return 'OK'
