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


class LIFOCache(BaseCaching):
    """
    The LIFOCache class inherits from the BaseCaching
    to implements several agrorithms for caching. This
    is a very basic on.
    """
    Last_insert = ''

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
        beyond maximum limit the last data is discarded.
        """

        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # last_key = list(self.cache_data.keys())[-2]
                del self.cache_data[LIFOCache.last_insert]
                print(f'DISCARD: {LIFOCache.last_insert}')
            LIFOCache.last_insert = key

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
