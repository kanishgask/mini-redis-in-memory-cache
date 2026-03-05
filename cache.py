import time

class CacheItem:
    def __init__(self, value, ttl=None):
        self.value = value
        self.expiry = time.time() + ttl if ttl else None

class MiniRedis:
    def __init__(self, max_size=100):
        self.store = {}
        self.max_size = max_size

    def set(self, key, value, ttl=None):
        if len(self.store) >= self.max_size:
            self.evict()
        self.store[key] = CacheItem(value, ttl)

    def get(self, key):
        item = self.store.get(key)
        if not item:
            return None
        if item.expiry and time.time() > item.expiry:
            del self.store[key]
            return None
        return item.value

    def delete(self, key):
        if key in self.store:
            del self.store[key]

    def evict(self):
        # Simple eviction: remove first key (can improve to LRU)
        if self.store:
            first_key = next(iter(self.store))
            del self.store[first_key]

# Demo
if __name__ == "__main__":
    cache = MiniRedis(max_size=3)
    cache.set("a", 1, ttl=5)
    cache.set("b", 2)
    cache.set("c", 3)
    print(cache.get("a"))
    cache.set("d", 4)  # triggers eviction
    print(cache.store.keys())
