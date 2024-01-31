#!/usr/bin/env python3
'''
This module houses a basic caching class.
'''
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    The MRUCache class inherits from the BaseCaching
    to implements several agrorithms for caching. This
    is a very basic on.
    """

    def __init__(self):
        """
        The first method to be called at the instantiation of the
        class
        """
        super().__init__()
        # self.occur = {}
        self.tk = ['']

    def put(self, key, item):
        """
        Adds a new item to the cache, if key and item is not None.
        otherwise, no action is taken. If at any point the cache goes
        beyond maximum limit the most recently used data is discarded.
        """

        # confirm the key is not none
        if key is not None and item is not None:

            # allocate the item to the key in the cache
            self.cache_data[key] = item

            # check if the cache is not over loaded
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:

                # delete the most recently used data which is tracked in
                # self.tk
                del self.cache_data[self.tk[0]]
                print(f'DISCARD: {self.tk[0]}')

                # once deletion happens the recently used key is tracked
                self.tk[0] = key

    def get(self, key):
        """
        Gets an item in the cache by the key, if the key is not None.
        If the key is not in the cached data, None is returned.
        """
        if key is not None:
            # Tracking usage of data same as in the put method
            if key in self.cache_data:
                self.tk[0] = key

            # The get method of dictionaries return None
            # if the key does not exists. But if it does, the
            # corresponding value is returned
            # print(self.occur)
            return self.cache_data.get(key)
        return None
