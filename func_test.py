import functions as f
import unittest

class Test(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    def test_add_ind(self):
        self.assertEqual(f.add(4,5), 9)

  
if __name__ == '__main__':
    unittest.main()