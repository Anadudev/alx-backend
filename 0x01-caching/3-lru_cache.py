#!/usr/bin/env python3
""" LRU Caching """
from base_caching import BaseCaching

tracker = []

class LRUCache(BaseCaching):
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        size = len(self.cache_data)
        if key and item:
            if size >= super().MAX_ITEMS and key in self.cache_data:
                for k, v in self.cache_data.items():
                    if k not in tracker:
                        print(f"DISCARD: {k}")
                        del self.cache_data[k]
                        break
            print(tracker)
            self.cache_data[key] = item

    def get(self, key):
        if key and key in self.cache_data:
            if key not in tracker:
                tracker.append(key)
            return self.cache_data[key]
        return None
