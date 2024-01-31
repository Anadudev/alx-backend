#!/usr/bin/env python3
""" LRU Caching """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """_summary_

    Args:
        BaseCaching (_type_): _description_
    """

    def __init__(self):
        """_summary_"""
        super().__init__()
        self.tracker = []

    def put(self, key, item):
        """_summary_

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        size = len(self.cache_data)
        if key and item:
            if key not in self.tracker:
                self.tracker.append(key)
            else:
                self.tracker.append(self.tracker.pop(self.tracker.index(key)))
            self.cache_data[key] = item
            if size >= super().MAX_ITEMS and key in self.cache_data:
                rid = self.tracker.pop(0)
                del self.cache_data[rid]
                print(f"DISCARD: {rid}")

    def get(self, key):
        """_summary_

        Args:
            key (_type_): _description_

        Returns:
            _type_: _description_
        """
        if key and key in self.cache_data:
            self.tracker.append(self.tracker.pop(self.tracker.index(key)))
            return self.cache_data[key]
        return None
