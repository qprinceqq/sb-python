from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    @property
    def least_recently_used(self):
        return next(iter(self.cache)) if self.cache else None

    @least_recently_used.setter
    def least_recently_used(self, new_elem):
        self.cache[new_elem[0]] = new_elem[1]
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def add_element(self, key, value):
        self.least_recently_used = (key, value)

    def get_element(self, key):
        if key in self.cache:
            self.least_recently_used = (key, self.cache.pop(key))
            return self.cache[key]
        else:
            return None

    def print_cache(self):
        for key, value in self.cache.items():
            print(f"{key} : {value}")

    def cache_info(self):
        return f"LRUCache(capacity={self.capacity}, size={len(self.cache)})"


cache = LRUCache(3)
cache.add_element('a', '1')
cache.add_element('b', '2')
cache.add_element('c', '3')
cache.print_cache()
print()
print('b:', cache.get_element('b'))
print()
cache.add_element('d', '4')
cache.print_cache()
print(cache.cache_info())
