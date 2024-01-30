#!/usr/bin/python3
""" BaseCaching module
"""


class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError(
            "put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError(
            "get must be implemented in your cache class")


class MRUCache(BaseCaching):
    """
    The MRUCache class inherits from the BaseCaching
    to implements several agrorithms for caching. This
    is a very basic on.
    """
    occur = {}

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
        beyond maximum limit the most recently used data is discarded.
        """

        if key is not None and item is not None:
            # check if the key is being tracked
            # everytime a key is used, it must be counted
            # to the MRUCache.occur so the statistics is taken
            # MRUCache.tk.append(key)
            MRUCache.occur[key] = MRUCache.occur.get(key, 0) + 1
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:

                # Check for similar occurence in the tracker
                # If there's none with a higher number, the most
                # recent is discarded
                if max(list(MRUCache.occur.values())) == 1:
                    most_used = list(MRUCache.occur.keys())[-1]

                # if not the most used should be discarded
                else:
                    most_used = max(MRUCache.occur, key=MRUCache.occur.get)
                del self.cache_data[most_used]
                del MRUCache.occur[most_used]
                print(f'DISCARD: {most_used}')

    def get(self, key):
        """
        Gets an item in the cache by the key, if the key is not None.
        If the key is not in the cached data, None is returned.
        """
        if key is not None:

            # Tracking usage of data same as in the put method
            if key in MRUCache.occur:
                MRUCache.occur[key] = MRUCache.occur.get(key, 0) + 1

            # The get method of dictionaries return None
            # if the key does not exists. But if it does, the
            # corresponding value is returned
            # print(MRUCache.occur)
            return self.cache_data.get(key)
        return None
