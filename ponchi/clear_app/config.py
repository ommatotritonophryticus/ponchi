TOKEN = ''

DATABASES = {
    'fake_db': {
        'type': 'ponchi.databases.fake_db',
    },
    'redis': {
        'type': 'ponchi.databases.redis',
        'host': 'localhost',
        'port': 6379,
        'decode_responses': True,
    }
}

DATABASE = DATABASES['fake_db']

'''
MIDDLEWARE = [
    'ponchi.contrib.statistic.statistic'
]
'''

LOG_LEVELS = {
    'debug': 10,
    'info': 20,
    'warning': 30,
    'error': 40,
    'critical': 50,
}

LOG_LEVEL = LOG_LEVELS['info']

LOG_CONFIGS = {
    'in_file': {
        'filename': 'ponchi.log',
        'level': LOG_LEVEL,
        'filemode': 'w'
    },
    'in_console': {
        'level': LOG_LEVEL
    }
}

LOG_CONFIG = LOG_CONFIGS['in_console']
