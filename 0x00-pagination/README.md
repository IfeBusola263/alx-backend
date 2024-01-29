## PAGINATION
In this project i show:

> How to paginate a dataset with simple page and page_size parameters.
---
> How to paginate a dataset with hypermedia metadata.
---
> How to paginate in a deletion-resilient manner.
---
* 0-simple_helper_function.py
```
Function named index_range that takes two integer arguments page and page_size.

The function should return a tuple of size two containing a start index
and an end index corresponding to the range of indexes
to return in a list for those particular pagination parameters.
```

* 1-simple_pagination.py
```
Implements a Server class, with a method to get data from
the csv, based on the correct range.
```

* 2-hypermedia_pagination.py
```
Implement a get_hyper method that takes the same arguments
(and defaults) as get_page and returns a dictionary containing
the following key-value pairs:

> page_size: the length of the returned dataset page
> page: the current page number
> data: the dataset page (equivalent to return from previous task)
> next_page: number of the next page, None if no next page
> prev_page: number of the previous page, None if no previous page
> total_pages: the total number of pages in the dataset as an integer
```

* 3-hypermedia_del_pagination.py
```
Implements another Server class, The goal here is that if between two queries,
certain rows are removed from the dataset, the user does not miss items
from dataset when changing page.

The get_hyper_index method has two integer arguments: index with a
None default value and page_size with default value of 10.

The method returns a dictionary with the following key-value pairs:

> index: the current start index of the return page.
That is the index of the first item in the current page.
For example if requesting page 3 with page_size 20,
and no data was removed from the dataset, the current index should be 60.

> next_index: the next index to query with. That should be the index of the
first item after the last item on the current page.

> page_size: the current page size
> data: the actual page of the dataset
```