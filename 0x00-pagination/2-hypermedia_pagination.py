#!/usr/bin/env python3
"""
task 2
"""

import math
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """index range"""
    return ((page - 1) * page_size, page * page_size)


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
        """
        Get a page of data from the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        self.dataset()
        start, end = index_range(page, page_size)
        return self.__dataset[start:end]

    def get_hyper(self, page: int, page_size: int) -> tuple:
        """
        task 2
        """
        prev_page = 0
        next_page = 0
        total_pages = Server.dataset(self)
        if page - 1 > 0:
            prev_page = page - 1
        else:
            prev_page = None
        if (page + 1) < total_pages:
            next_page = page + 1
        else:
            next_page = None

        dict_ = {}
        dict_["page_size"] = page_size,
        dict_["page"] = page
        dict_["data"] = Server.get_page(page, page_size)
        dict_["next_page"]: next_page
        dict_["prev_page"]: prev_page
        dict_["total_pages"]: total_pages

        return dict_
