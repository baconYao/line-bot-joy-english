import os

# 3rd
from flask import abort
from flask_pymongo import PyMongo

# our
from app.log import logging_util

logger = logging_util.get_logger(__name__)
mongo = PyMongo()


def init_db(app):
    app.logger.info('Initializing Database...')
    DB_URI = os.getenv('DB_URI', None)
    if not DB_URI:
        app.logger.error('No DB_URI env!')
        abort(500)

    app.config['MONGO_URI'] = DB_URI
    mongo.init_app(app=app)
    app.logger.info('Initialized Database')


def get_all_phrases_from_db():
    ''' Get all phrases from Database
    '''
    logger.info('Getting all phrases from DB...')
    phrases = mongo.db['phrase'].find()
    return [p for p in phrases]
