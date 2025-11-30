import unittest
from simple_calculator import SimpleCalculator

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self): 
        self.assertEqual(self.calc.add(10,5), 15)  
        self.assertEqual(self.calc.add(-1, 1), 0) 
        self.assertEqual(self.calc.add(2, 3), 5)


    def test_subtraction(self): 
        self.assertEqual(self.calc.subtract(10,5), 5)
        self.assertEqual(self.calc.subtract(10,13), -3)
        self.assertEqual(self.calc.subtract(1,5), -4)


    def test_multiply(self): 
        self.assertEqual(self.calc.multiply(10,5), 50)
        self.assertEqual(self.calc.multiply(10,-5), -50)
        self.assertEqual(self.calc.multiply(1,-1), -1)


    def test_divide(self): 
        self.assertEqual(self.calc.divide(10,5), 2) 
        self.assertEqual(self.calc.divide(10,1), 10) 
if __name__ =='__main__':
    unittest.main()  

