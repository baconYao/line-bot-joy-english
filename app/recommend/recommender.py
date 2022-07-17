# system
import random

# our
from app.cache.cache import cache, CACHE_ALL_PHRASE


def get_daily_recommended_phrases():
    ''' Get the daily recommended phrases
    '''
    phrases = cache.get(CACHE_ALL_PHRASE)
    n = len(phrases)
    pps = []
    for i in range(3):
        pps.append(phrases[random.randrange(0, n)])
    text = phrases_formatter(phrases=pps)
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
