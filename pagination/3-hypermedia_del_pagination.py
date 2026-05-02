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
        # 1. Tipin int olduğunu və indeksin orijinal məlumatın limitlərində olduğunu yoxlayırıq
        assert type(index) == int and type(page_size) == int
        assert 0 <= index < len(self.dataset())

        indexed_data = self.indexed_dataset()
        data = []
        current_index = index

        # 2. Döngü limitini dictionary-nin deyil, orijinal datanın uzunluğuna (len(self.dataset())) bağlayırıq
        while len(data) < page_size and current_index < len(self.dataset()):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        # 3. next_index birbaşa dayandığımız son index olur
        return {
            'index': index,
            'next_index': current_index,
            'page_size': len(data),
            'data': data
        }
