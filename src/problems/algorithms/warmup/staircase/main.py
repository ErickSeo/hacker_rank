#!/bin/python3
#https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true

class Staircase:
    def __init__(self, size: int):
        self.size = size
    
    def build(self):
        for i in range(self.size):
            space: str = (self.size-i-1)*" "
            content: str = (i+1)*"#"
            print(space+content)

if __name__ == '__main__':
    n = int(input().strip())
    staircase = Staircase(size=n)
    staircase.build()
