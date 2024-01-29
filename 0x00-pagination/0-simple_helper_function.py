#!/usr/bin/env python3
'''
This module has a helper function "index_range" that
returns a tuple containing the starting index and ending index
corresponding to the range of indexes to return in a list for
the given pagination parameters(page and page_size).
'''
from typing import Tuple


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
