#!/usr/bin/env python3
""" Simple helper function """
from typing import Tuple


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
