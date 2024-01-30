#!/usr/bin/env python3
'''
This module houses a basic caching class.
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    The BasicCache class inherits from the BaseCaching
    to implements several agrorithms for caching. This
    is a very basic on.
    """

    def put(self, key, item):
        """
        Adds a new item to the cache, if key and item is not None.
        otherwise, no action is taken
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets an item in the cache by the key, if the key is not None.
        If the key is not in the cached data, None is returned.
        """
        if key is not None:

            # The get method of dictionaries return None
            # if the key does not exists. But if it does, the
            # corresponding value is returned
            return self.cache_data.get(key)
        return None
