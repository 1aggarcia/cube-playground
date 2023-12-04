import unittest
from modelos import cubo

class ProbarCubo(unittest.TestCase):

    def test_basico(self):
        self.assertEqual(2+2, 4)

if __name__ == '__main__':
    unittest.main()