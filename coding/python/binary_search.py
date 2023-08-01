#!/usr/bin/env python

import random
from typing import List


def binary_search(arr: List[int], low: int, high: int, x: int) -> int:
    """
    A Binary Search Example which has O(log n) time complexity.
    """
    if low <= high:
        mid: int = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binary_search(arr, mid + 1, high, x)
        else:
            return binary_search(arr,low, mid - 1, x)
    else:
        return -1


if __name__ == '__main__':
    rand_num_li: List[int] = sorted([random.randint(1, 50) for _ in range(10)])
    x: int = random.randint(1, 50)
    print("List: {}\nTarget: {}\nIndex: {}".format(
        rand_num_li, x,
        binary_search(rand_num_li, 0, len(rand_num_li) - 1, x)))
