#!/usr/bin/env python3
""" FIFO caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        a class FIFOCache that inherits from BaseCaching
        and is a caching system
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key key"""
        if key and item:
            if len(self.cache_data) >= super().MAX_ITEMS \
                    and key not in self.cache_data:
                discarded = list(self.cache_data)[-1]
                print(f"DISCARD: {discarded}")
                del self.cache_data[discarded]
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
