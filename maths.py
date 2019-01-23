import unittest

def fibonacci(n: int, c: dict = {}) -> int:
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    if not n in c:
        c[n] = fibonacci(n-1, c) + fibonacci(n-2, c)
    return c[n]
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError('factorial for {} does not exist'.format(n))
    elif n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
def nCk(n: int, k: int) -> int:
    if n < k:
        raise ValueError('n cannot be smaller than k')
    if n < 0 or k < 0:
        raise ValueError('n and k must be larger than 0')
    return factorial(n)/(factorial(k)*factorial(n-k))

class TestMath(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual([0, 1, 1, 2, 3, 5, 8, 13, 21], [fibonacci(x) for x in range(1,10)])
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(-1), 0)
    def test_factorial(self):
        self.assertEqual([1, 1, 2, 6, 24, 120, 720, 5040, 40320], [factorial(x) for x in range(0,9)])
        with self.assertRaises(ValueError): factorial(-1)
    def test_nCk(self):
        self.assertEqual(nCk(4,2), 6)
        self.assertEqual(nCk(5,5), 1)
        self.assertEqual(nCk(5,0), 1)
        with self.assertRaises(ValueError): nCk(1, 5)
        with self.assertRaises(ValueError): nCk(-1, -4)

if __name__ == '__main__':
    unittest.main()