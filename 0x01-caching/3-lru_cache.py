#!/usr/bin/env python3
'''
This module houses a basic caching class.
'''
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    The LRUCache class inherits from the BaseCaching
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

    def put(self, key, item):
        """
        Adds a new item to the cache, if key and item is not None.
        otherwise, no action is taken. If at any point the cache goes
        beyond maximum limit the last recently used data is discarded.
        """

        if key is not None and item is not None:
            # check if the key is being tracked
            # everytime a key is used, it must be popped and appended
            # to the LRUCache.tk so the least used would be at the top
            # of the list
            LRUCache.tk.append(
                LRUCache.tk.pop(LRUCache.tk.index(key)
                                ) if key in LRUCache.tk else key)

            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                del self.cache_data[LRUCache.tk[0]]

                # remove it from the tracker and print it
                print(f'DISCARD: {LRUCache.tk.pop(0)}')

    def get(self, key):
        """
        Gets an item in the cache by the key, if the key is not None.
        If the key is not in the cached data, None is returned.
        """
        if key is not None:
            if key in LRUCache.tk:
                LRUCache.tk.append(LRUCache.tk.pop(LRUCache.tk.index(key)))

            # The get method of dictionaries return None
            # if the key does not exists. But if it does, the
            # corresponding value is returned
            return self.cache_data.get(key)
        return None
