import os

class BigSum:
    def __init__(self, numbers):
        self._numbers = numbers

    def calculate_sum(self):
        return sum(self._numbers)

def main():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    big_sum = BigSum(ar)
    result = big_sum.calculate_sum()

    fptr.write(str(result) + '\n')
    fptr.close()

if __name__ == '__main__':
    main()
