object_pool
===========

object_poll is a simple thread-safe generic python object pool. Typical use:

import memcache
import object_pool

memcache_pool = ObjectPool(lambda: memcache.Client(['127.0.0.1:11211']), max_size=10)
with memcache_pool.item() as memcache:
    memcache.set(b'key', b'value')

with is not required:

try:
    memcache = memcache_pool.get()
finally:
    memcache_pool.put(memcache)

It supports a timeout argument as well:

try:
    memcache = memcache_pool.get(timeout=1.0)
except ObjectPoolTimeout:
    import logging
    logging.warning('timed out trying to get memcache connection')
