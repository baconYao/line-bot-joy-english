# 3rd
from flask import Flask

# our
from src.cache.cache import cache, cache_config
from src.db.db import init_db
from src.bot import line_bot_bp

app = Flask(__name__)
# Init cache
cache.init_app(app, config=cache_config)
# Init db
init_db()


@app.route('/')
def index():
    return 'success佈署!!'


# callback endpoint for line bot.
# It will be https://xxxxx/line-bot/callback
app.register_blueprint(line_bot_bp)

if __name__ == '__main__':
    from argparse import ArgumentParser
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
