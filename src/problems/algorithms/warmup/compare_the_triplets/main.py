#!/bin/python3

import os
from typing import List

class Player:
    def __init__(self, 
                 name: str,
                 triplets: List[int]):
        self._name: str = name
        self._triplets: List[int] = triplets
        self._score: int = 0
    
    @property
    def score(self) -> int:
        return self._score

    def get_point(self, index: int):
        return self._triplets[index]
    
    def add(self):
        self._score += 1

class Triplets:
    def __init__(self,
                 AliceTriplets: List[int],
                 BobTriplets: List[int] ):
        self._alice = Player(name="Alice", triplets=AliceTriplets)
        self._bob = Player(name="Bob", triplets=BobTriplets)

    def compare(self) -> List[int]:
        for i in range(3):
            if self._alice.get_point(i) > self._bob.get_point(i):
                self._alice.add()
            if self._bob.get_point(i) > self._alice.get_point(i):
                self._bob.add()
        return [self._alice.score, self._bob.score]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    alice: List[int] = list(map(int, input().rstrip().split()))

    bob: List[int] = list(map(int, input().rstrip().split()))

    triplets: Triplets = Triplets(alice, bob)

    result: List[int] = triplets.compare()

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
