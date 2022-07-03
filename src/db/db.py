import json

# our
from src.cache.cache import cache


def get_example_from_dummy_db_to_cache():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    print('Get English phrases from dummy json to cache...')

    # FIXME: Load out Exglish Example to cache
    with open('src/db/dummy.json', encoding='UTF-8') as f:
        english_data = json.load(f)
        cache.set('all_english_phrases', english_data)


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    print('close database successfully')


def init_db():
    """Clear existing data and create new tables."""
    print('Initializing database ...')
    get_example_from_dummy_db_to_cache()
    print('Initialized database successfully')
