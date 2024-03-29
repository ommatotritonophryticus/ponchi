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
