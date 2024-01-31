#!/usr/bin/env python3
"""  LIFO Caching """
from base_caching import BaseCaching
from time import time


tracker = 1


class LIFOCache(BaseCaching):
    """
    a class LIFOCache that inherits from
    BaseCaching and is a caching system
    """

    def __init__(self):
        """_summary_"""
        super().__init__()

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        global tracker
        if key and item:
            index = len(self.cache_data)
            if index >= super().MAX_ITEMS and key not in self.cache_data:
                print(f"DISCARD: {list(self.cache_data)[index - tracker]}")
                del self.cache_data[list(self.cache_data)[index - tracker]]
                tracker += 1
                if tracker > 2:
                    tracker = 1
            self.cache_data[key] = item

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
        return None
