#!/bin/python3
#https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

import os
from typing import List
class Cake:
    def __init__(self, candles: List[int]):
        self.candles_high: List[int] = candles
    
    def blow(self) -> int:
        higher_candle: int = max(self.candles_high)
        return self.candles_high.count(higher_candle)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    cake = Cake(candles=candles)
    result = cake.blow()

    fptr.write(str(result) + '\n')

    fptr.close()
