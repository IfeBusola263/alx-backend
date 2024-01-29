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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        This method returns a dictionary containing:
        page_size: the length of the returned dataset page
        page: the current page number
        data: the dataset page (equivalent to return from previous task)
        next_page: number of the next page, None if no next page
        prev_page: number of the previous page, None if no previous page
        total_pages: the total number of pages in the dataset as an integer

        >>> server = Server()
        >>> print(server.get_hyper(1, 2)) # Assuming you had a csv file
        {'page_size': 2, 'page': 1,
        'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER',
        'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER',
        'Chloe', '112', '2']], 'next_page': 2, 'prev_page': None,
        'total_pages': 9709}
        '''
        data = self.get_page(page, page_size)
        # start, end = index_page(page, page_size)
        next_page = 0
        prev_page = 0
        total_page = math.ceil(len(self.dataset()) / page_size)
        if data == []:
            page_size = 0

        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None

        if total_page < page:
            next_page = None
        else:
            next_page = page + 1

        return {'page_size': page_size, 'page': page, 'data': data,
                'next_page': next_page, 'prev_page': prev_page,
                'total_page': total_page}
