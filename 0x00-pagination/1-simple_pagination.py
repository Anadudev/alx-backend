#!/usr/bin/env python3
""" Simple pagination """
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """a function that takes two
    integer arguments page and page_size

    Args:
        page (int): page i number
        page_size (int): page size in number

    Returns:
        Tuple[int, int]: return a tuple of size two
    containing a start index and an end index
    """
    return ((page - 1) * page_size, page_size * page)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """method that gets a page in a pagination

        Args:
            page (int, optional): tha page to be gotten. Defaults to 1.
            page_size (int, optional): total page size. Defaults to 10.

        Returns:
            List[List]:  the appropriate page of the dataset
            (i.e. the correct list of rows)
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page, page_size) and page_size > 10
        data = self.dataset()
        try:
            p, size = index_range(page, page_size)
            return data[p, size]
        except IndexError:
            return []
