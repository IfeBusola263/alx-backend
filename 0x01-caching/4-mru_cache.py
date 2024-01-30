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
        self.occur = {}

    def put(self, key, item):
        """
        Adds a new item to the cache, if key and item is not None.
        otherwise, no action is taken. If at any point the cache goes
        beyond maximum limit the most recently used data is discarded.
        """

        if key is not None and item is not None:
            # check if the key is being tracked
            # everytime a key is used, it must be counted
            # to the self.occur so the statistics is taken
            # MRUCache.tk.append(key)
            self.occur[key] = self.occur.get(key, 0) + 1
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:

                # Check for similar occurence in the tracker
                # If there's none with a higher number, the most
                # recent is discarded
                if max(list(self.occur.values())) == 1:
                    most_used = list(self.occur.keys())[-1]

                # if not the most used should be discarded
                else:
                    most_used = max(self.occur, key=self.occur.get)
                del self.cache_data[most_used]
                del self.occur[most_used]
                print(f'DISCARD: {most_used}')


    def get(self, key):
        """
        Gets an item in the cache by the key, if the key is not None.
        If the key is not in the cached data, None is returned.
        """
        if key is not None:

            # Tracking usage of data same as in the put method
            if key in self.occur:
                self.occur[key] = self.occur.get(key, 0) + 1

            # The get method of dictionaries return None
            # if the key does not exists. But if it does, the
            # corresponding value is returned
            # print(self.occur)
            return self.cache_data.get(key)
        return None
