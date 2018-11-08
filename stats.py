from math import factorial
from unittest import TestCase, main
def bino(n, k):
    return factorial(n)/(factorial(k)*factorial(n-k))
def bino_mass(n, x, p):
    return bino(n,x)*(p**x)*((1-p)**(n-x))
def bino_dist(n, p, start, end):
    return sum(bino_mass(n, x, p) for x in range(start,end+1))
class MathShit(TestCase):
    def test_bino_dist(self):
        self.assertAlmostEqual(0.0197, bino_dist(10, 3/4, 0, 4), 4)
        self.assertAlmostEqual(3/8, bino_dist(4, 1/2, 2, 2), 4)

if __name__ == '__main__':
    main()