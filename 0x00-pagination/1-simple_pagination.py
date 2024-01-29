#!/usr/bin/env python3
'''
This is a module for the Server Class.
'''

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    This function returns a tuple containg the starting index and ending
    index corresponding to the number of items on the page "page_size",
    if you are requesting the page number "page".
    '''

    # Get the starting index based on the paage and number of
    # items on each page
    starting_index = (page - 1) * page_size

    # The ending index would be an additon of the page_size
    # or number of items to the starting index
    ending_index = starting_index + page_size
    return (starting_index, ending_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        This method returns the list of dataset based on the index range.
        otherwise, an empty list.
        '''

        # Validate the type of the input
        assert (type(page) == int and type(page_size) == int)

        # Validate inputs are not negative values
        assert (page > 0 and page_size > 0)

        # Get the range on the page
        start, end = index_range(page, page_size)

        # Return the page if index is not out of range
        # if it is return empty list
        try:
            return self.dataset()[start:end]
        except IndexError:
            return []
