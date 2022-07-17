# 3rd
from flask_caching import Cache

# our
from app.db.db import get_all_phrases_from_db
from app.log import logging_util

logger = logging_util.get_logger(__name__)

CACHE_ALL_PHRASE = 'all_phrases'
CACHE_DAILY_PHRASE = 'daily_phrases'

cache_config = {
    'DEBUG': True,  # some Flask specific configs
    'CACHE_TYPE': 'SimpleCache',  # Flask-Caching related configs
    'CACHE_DEFAULT_TIMEOUT': 10800  # 3600 * 30 (unit: second)
}

cache = Cache()


def init_cache(app):
    ''' Initialize the cache
    '''
    app.logger.info('Initializing Cache...')
    cache.init_app(app, config=cache_config)
    app.logger.info('Initialized Cache')


def inject_cache(key='', value=None):
    ''' Inject cache value

        @params:
            key: the string of key in cahce
            value: the value in cahce for specific key
    '''
    if not key or not value:
        logger.warn(
            'Invalid key or value while injecting cache. key: {}, value: {}'.
            format(key, value))

    cache.delete(key)
    cache.set(key, value)


def retrieve_data_from_cache(key=''):
    ''' Get the cached data

        @params:
            key: the string of key in cahce which you want to retrieve
    '''
    if not key:
        logger.warn('Invalid key while retrieve data from cache.')

    return cache.get(key)


def cache_all_phrases():
    ''' Be used cache all phrases
    '''
    logger.info('Caching all phrases...')
    # Get phrases from DB
    phrases = get_all_phrases_from_db()
    inject_cache(CACHE_ALL_PHRASE, phrases)


def get_all_phrases_from_cache():
    ''' Be used to cache all phrases
    '''
    return retrieve_data_from_cache(CACHE_ALL_PHRASE)
