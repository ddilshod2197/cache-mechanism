class Cache:
    def __init__(self, size):
        self.size = size
        self.cache = {}

    def get(self, key):
        if key in self.cache:
            return self.cache[key]
        else:
            return None

    def set(self, key, value):
        if key in self.cache:
            self.cache[key] = value
        elif len(self.cache) < self.size:
            self.cache[key] = value
        else:
            self.cache.popitem(last=False)
            self.cache[key] = value

    def delete(self, key):
        if key in self.cache:
            del self.cache[key]

    def clear(self):
        self.cache.clear()

    def get_size(self):
        return len(self.cache)

    def get_keys(self):
        return list(self.cache.keys())

# Misol foydalanish:
cache = Cache(5)
cache.set('key1', 'value1')
cache.set('key2', 'value2')
cache.set('key3', 'value3')
cache.set('key4', 'value4')
cache.set('key5', 'value5')

print(cache.get('key1'))  # value1
print(cache.get('key2'))  # value2
print(cache.get('key3'))  # value3
print(cache.get('key4'))  # value4
print(cache.get('key5'))  # value5

cache.delete('key2')
print(cache.get('key2'))  # None

cache.clear()
print(cache.get_size())  # 0
