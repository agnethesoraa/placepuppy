from flask.ext.cache import Cache

config = {'CACHE_TYPE': 'simple'}
cache = Cache(config=config)
