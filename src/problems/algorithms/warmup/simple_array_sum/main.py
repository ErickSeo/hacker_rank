#!/bin/python3

import os
from typing import List

class SimpleArraySum:
    def __init__(self):
        self._numbers: List[int] = []
    
    @property
    def numbers(self) -> List[int]:
        return self._numbers
    
    @numbers.setter
    def numbers(self, number: int):
        self._numbers.append(number)
    
    def total(self) -> int:
        return sum(self._numbers)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    array_len = int(input().strip())

    numbers = list(map(int, input().rstrip().split()))

    simple_array = SimpleArraySum()

    for i in numbers:
        simple_array.numbers = i

    fptr.write(str(simple_array.total()) + '\n')

    fptr.close()
