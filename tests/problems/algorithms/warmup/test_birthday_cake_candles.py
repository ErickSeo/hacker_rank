from src.problems.algorithms.warmup.birthday_cake_candles.main import Cake

def test_cake():
    # Test Case 1
    candles1 = [4, 4, 1, 3]
    cake1 = Cake(candles=candles1)
    assert cake1.blow() == 2

    # Test Case 2
    candles2 = [1, 1, 1, 1]
    cake2 = Cake(candles=candles2)
    assert cake2.blow() == 4

    # Test Case 3
    candles3 = [3, 2, 1, 3, 3, 5]
    cake3 = Cake(candles=candles3)
    assert cake3.blow() == 1

    # Test Case 4
    candles4 = [7, 7, 7, 7]
    cake4 = Cake(candles=candles4)
    assert cake4.blow() == 4

if __name__ == "__main__":
    test_cake()
    print("All test cases passed!")
