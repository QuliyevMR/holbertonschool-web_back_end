#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary of pagination data that is resilient to
        deletions in the dataset.
        """
        dataset = self.indexed_dataset()
        
        # 1. Yalnız index-i və onun cari dataset açarlarına uyğunluğunu yoxlayırıq
        assert index is not None and index >= 0 and index <= max(dataset.keys())

        data = []
        current_index = index

        # 2. Döngü limitini dataset-in ən böyük açarına (key) bağlayırıq
        while len(data) < page_size and current_index <= max(dataset.keys()):
            if current_index in dataset:
                data.append(dataset[current_index])
            current_index += 1

        # 3. next_index təyini
        next_index = current_index if current_index <= max(dataset.keys()) else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }
