#!/usr/bin/env python3
'''
This module houses a basic caching class.
'''
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    The LFUCache class inherits from the BaseCaching
    to implements several agrorithms for caching. This
    is a very basic on.
    """
    tk = []

    def __init__(self):
        """
        The first method to be called at the instantiation of the
        class
        """
        super().__init__()
        self.freq = {}

    def put(self, key, item):
        """
        Adds a new item to the cache, if key and item is not None.
        otherwise, no action is taken. If at any point the cache goes
        beyond maximum limit the last recently used data is discarded.
        """

        if key is not None and item is not None:
            # check if the key is being tracked
            # everytime a key is used, it must be popped and appended
            # to the LFUCache.tk so the least used would be at the top
            # of the list
            LFUCache.tk.append(
                LFUCache.tk.pop(LFUCache.tk.index(key)
                                ) if key in LFUCache.tk else key)
            self.freq[key] = self.freq.get(key, 0) + 1

            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.freq.get(LFUCache.tk[0]) > 1:
                    to_delete = LFUCache.tk.pop(-1)
                    del self.cache_data[to_delete]
                    del self.freq[to_delete]
                else:
                    to_delete = LFUCache.tk.pop(0)
                    del self.freq[to_delete]

                # remove it from the tracker and print it
                print(f'DISCARD: {to_delete}')

    def get(self, key):
        """
        Gets an item in the cache by the key, if the key is not None.
        If the key is not in the cached data, None is returned.
        """
        if key is not None:
            if key in LFUCache.tk:
                LFUCache.tk.append(LFUCache.tk.pop(LFUCache.tk.index(key)))

            if key in self.freq:
                self.freq[key] = self.freq.get(key, 0) + 1

            # The get method of dictionaries return None
            # if the key does not exists. But if it does, the
            # corresponding value is returned
            return self.cache_data.get(key)
        return None
