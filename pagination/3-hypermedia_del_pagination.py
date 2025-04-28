#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Optional


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
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
            assert index is not None and isinstance(index, int)
            assert index >= 0 and index < len(self.indexed_dataset())

            dataset = self.indexed_dataset()
            data = []
            current_index = index
            collected = 0

            while collected < page_size and current_index < len(self.dataset()):
                item = dataset.get(current_index)
                if item is not None:
                    data.append(item)
                    collected += 1
                    current_index += 1

            return {
                "index": index,
                "next_index": current_index,
                "page_size": len(data),
                "data": data
            }
