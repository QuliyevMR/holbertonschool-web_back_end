#!/usr/bin/env python3
"""
Simple pagination module.
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for a given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


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
        Finds the correct indexes to paginate the dataset and returns
        the appropriate page of the dataset.
        """
        # Verify that both arguments are integers greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Get the range of indexes
        start, end = index_range(page, page_size)

        # Retrieve the dataset
        data = self.dataset()

        # If start index is out of range, return an empty list
        if start >= len(data):
            return []

        # Return the slice of the dataset
        return data[start:end]
