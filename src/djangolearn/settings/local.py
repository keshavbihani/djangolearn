from .base import *
import redis

# Broker settings
BROKER_URL = "redis://localhost:6379"
BROKER_HEARTBEAT = 30
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 15 * 60}  # 15 mins

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangolearndb',
        'USER': 'mydjangolearnuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}


REDIS_DB = redis.StrictRedis(host='localhost', port=6379, db=0)
REDIS_DB_WRITE = redis.StrictRedis(host='localhost', port=6379, db=0)
