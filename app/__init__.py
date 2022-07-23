# 3 rd
from flask import Flask

# our
from .log import logging_util
from .recommend.recommender import run_scheduler
# logger should be init before importing our ohter moudles
logging_util.init()

from .cache.cache import cache_all_phrases, init_cache  # noqa: E402
from .db.db import init_db  # noqa: E402

from .bot import line_bot_bp    # noqa: E402


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    # Init db
    init_db(app)
    # Init cache
    # cache.init_app(app, config=cache_config)
    init_cache(app)
    cache_all_phrases()
    run_scheduler()

    @app.route('/')
    def index():
        return 'success佈署~~~'

    # callback endpoint for line bot.
    # It will be https://xxxxx/line-bot/callback
    app.register_blueprint(line_bot_bp)

    return app
