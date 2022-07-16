import logging
import logging.config

DICT_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format':
            '%(levelname)-5s %(asctime)-15s - %(module)-15s: %(funcName)s ' +
            '%(lineno)-4d - %(message)s',
        }
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            # 'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default',
            'stream': 'ext://sys.stdout',
            'level': 'DEBUG'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
}


def init():
    logging.config.dictConfig(DICT_CONFIG)


def get_logger(module_name):
    return logging.getLogger('root').getChild(module_name)
