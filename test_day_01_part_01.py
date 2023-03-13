import unittest
from day_01_part_01 import *

class Test_01_01(unittest.TestCase):

    def test1(self):
        address="test_input_01"
        self.assertEqual(read_input(address) , [141107 , 119016, 145241 , 72264, 116665])

    def test2(self):
        self.assertEqual(sum_fuels([22]),5 )
    

    def test3(self):
        self.assertEqual(sum_fuels([22, 24]), 11)
    

    def test4(self):
        self.assertEqual(sum_fuels([22, 24 , 1981]) , 669)
    

    def test5(self):
        self.assertEqual(sum_fuels([22, 24 , 1981 , 141107]) , 47702)

    
    def test6(self):
        input_fuel=read_input("test_input_01")
        self.assertEqual(sum_fuels(input_fuel) , 198086)




if __name__ == '__main__':
    unittest.main(verbosity=2)

    