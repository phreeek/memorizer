from flask_cache import Cache

from memorizer.config import CACHE_TYPE, CACHE_REDIS_URL

cache = Cache(config={
    'CACHE_TYPE': CACHE_TYPE,
    'CACHE_KEY_PREFIX': 'memorizer',
    'CACHE_REDIS_URL': CACHE_REDIS_URL
})
