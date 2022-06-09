import unittest
from MyMathModule import is_prime
from MyMathModule import plus
from MyMathModule import divide

class testcaseSample(unittest.TestCase):

    def test_prime1(self):
        self.assertFalse(is_prime(10))

    def test_prime2(self):
        self.assertTrue(is_prime(5))

    def test_plus(self):
        self.assertEquals((plus(5,6)),11)
    
    def test_divide(self):
        self.assertEqual((divide(5,1)),5)

if __name__ == '__main__':
    unittest.main()
    