import time
from cache import MiniRedis

def ttl_eviction_demo():
    cache = MiniRedis(max_size=5)
    cache.set("key1", "value1", ttl=2)
    cache.set("key2", "value2", ttl=4)

    while True:
        print({k: cache.get(k) for k in cache.store.keys()})
        time.sleep(1)

if __name__ == "__main__":
    ttl_eviction_demo()
