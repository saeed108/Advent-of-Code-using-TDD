import unittest
from day_01_part_02 import multi_fuel


class test_01_02(unittest.TestCase):


    def test7(self):

        self.assertEqual(multi_fuel([22]) , 5)

    
    def test8(self):
        self.assertEqual(multi_fuel([22 , 24]) , 11)
    

    def test9(self):
        self.assertEqual(multi_fuel([22 , 24 , 1981]) , 982)
    

    def test_10(self):
        self.assertEqual(multi_fuel([22 , 24 , 1981, 141107]), 71502)
    

    def test_11(self):
        self.assertEqual(multi_fuel([22 , 24 , 1981, 141107 , 119016]) ,  130979)
    

if __name__ == '__main__':
    unittest.main(verbosity=2)