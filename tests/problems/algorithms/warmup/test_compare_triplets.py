import unittest
from src.problems.algorithms.warmup.compare_the_triplets.main import Triplets

class TestTriplets(unittest.TestCase):
    def test_compare(self):
        # Caso de teste 1: Alice vence em todos os triplets
        alice_triplets = [5, 6, 7]
        bob_triplets = [3, 2, 1]
        game = Triplets(AliceTriplets=alice_triplets, BobTriplets=bob_triplets)
        resultado = game.compare()
        self.assertEqual(resultado, [3, 0])  # Alice ganha 3 vezes, Bob não ganha nenhuma

        # Caso de teste 2: Bob vence em todos os triplets
        alice_triplets = [1, 2, 3]
        bob_triplets = [4, 5, 6]
        game = Triplets(AliceTriplets=alice_triplets, BobTriplets=bob_triplets)
        resultado = game.compare()
        self.assertEqual(resultado, [0, 3])  # Alice não ganha nenhuma, Bob ganha 3 vezes

        # Caso de teste 3: Empate em todos os triplets
        alice_triplets = [1, 2, 3]
        bob_triplets = [1, 2, 3]
        game = Triplets(AliceTriplets=alice_triplets, BobTriplets=bob_triplets)
        resultado = game.compare()
        self.assertEqual(resultado, [0, 0])  # Empate em todos os triplets

        # Caso de teste 4: Alice e Bob ganham alternadamente
        alice_triplets = [1, 3, 1]
        bob_triplets = [2, 2, 2]
        game = Triplets(AliceTriplets=alice_triplets, BobTriplets=bob_triplets)
        resultado = game.compare()
        self.assertEqual(resultado, [1, 2])  # Alice ganha 1 vez, Bob ganha 2 vezes

        # Caso de teste 5: Triplets aleatórios
        alice_triplets = [4, 7, 2]
        bob_triplets = [6, 3, 8]
        game = Triplets(AliceTriplets=alice_triplets, BobTriplets=bob_triplets)
        resultado = game.compare()
        self.assertEqual(resultado, [1, 2])

if __name__ == '__main__':
    unittest.main()
