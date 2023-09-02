#!/bin/python3
# https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=false

import os
from typing import List

class DiagonalDifference:
    def __init__(self, arr: List[int]):
        self.arr: List[int] = arr

    def calculate(self) -> int:
        n: int = len(self.arr)
        primary_sum: int = 0
        secondary_sum: int = 0
        
        for i in range(n):
            primary_sum += self.arr[i][i]
            secondary_sum += self.arr[i][n - 1 - i]
        
        return abs(primary_sum - secondary_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = DiagonalDifference(arr)

    fptr.write(str(result.calculate()) + '\n')

    fptr.close()
