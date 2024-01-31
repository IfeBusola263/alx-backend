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

            # insert the data into the cache
            self.cache_data[key] = item

            # confirm the cache is not overloaded
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:

                # sort the tracker to have least frequently used at the
                # top of the list
                lfu_order = sorted(self.freq.items(), key=lambda x: x[1])
                lfu_key = lfu_order[0][0]
                # print(self.freq)
                # print(lfu_order)

                # delete the least frequently used data in the cache
                del self.cache_data[lfu_key]
                print(f'DISCARD: {lfu_key}')

                # delete it from the tracker as well
                del self.freq[lfu_key]

            # Update the tracker with recent addition
            self.freq[key] = self.freq.get(key, 0) + 1

    def get(self, key):
        """
        Gets an item in the cache by the key, if the key is not None.
        If the key is not in the cached data, None is returned.
        """
        if key is not None:
            if key in self.cache_data:
                # tracking data from here too
                self.freq[key] = self.freq.get(key) + 1

            # The get method of dictionaries return None
            # if the key does not exists. But if it does, the
            # corresponding value is returned
            return self.cache_data.get(key)
        return None
