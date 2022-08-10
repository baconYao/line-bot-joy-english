# system
import random
# from time import timezone
from apscheduler.schedulers.background import BackgroundScheduler
# from datetime import datetime

# our
from app.cache.cache import (
    cache,
    CACHE_DAILY_PHRASE,
    get_all_phrases_from_cache
)

scheduler = BackgroundScheduler(timezone="Asia/Taipei")
cache_id_pointer = 0
UPDATE_DURATION = 43200  # seconds


def update_cache_id_counter(all_phrases_length):
    '''Periodically refresh daily_phrases_cache's id counter
    '''
    global cache_id_pointer
    cache_id_pointer = random.randrange(0, all_phrases_length - 3)
    '''global cache_id_pointer
    if cache_id_counter < (all_phrases_length-3):
        cache_id_counter += 3
    else:
        cache_id_counter = 0
    '''


def run_scheduler():
    '''Start scheduler
    '''
    all_phrases_length = len(get_all_phrases_from_cache())
    scheduler.add_job(update_cache_id_counter,
                      'interval',
                      seconds=UPDATE_DURATION,
                      args=[all_phrases_length])
    scheduler.start()


def all_to_daily_cache():
    '''Load daily_phrases_cache from all_phrases_cache
    '''
    phrases = get_all_phrases_from_cache()

    global cache_id_pointer
    daily_phrases = []
    for i in range(cache_id_pointer, cache_id_pointer + 3):
        daily_phrases.append(phrases[i])
    cache.set(CACHE_DAILY_PHRASE, daily_phrases)


def get_daily_recommended_phrases():
    ''' Get the daily recommended phrases
    '''

    all_to_daily_cache()
    phrases = cache.get(CACHE_DAILY_PHRASE)
    '''n = len(phrases)
    pps = []
    for i in range(3):
        pps.append(phrases[random.randrange(0, n)])
    '''

    text = phrases_formatter(phrases)
    return text


def phrases_formatter(phrases=[]):
    ''' Format the message
    '''
    text = ''
    for p in phrases:
        text += '*' * 50 + '\n'
        text += '例句: {}\n'.format(p['phrase'])
        text += '{}\n'.format(p['cn'])
    return text
