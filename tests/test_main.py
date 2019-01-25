import unittest


def add(x,y):
    return x + y

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(add(1,2), 3)
