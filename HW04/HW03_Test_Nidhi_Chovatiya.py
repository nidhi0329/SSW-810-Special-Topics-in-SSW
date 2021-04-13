""" 
@author: Nidhi Chovatiya
CWID : 10457344
    Implement a test class for fractions to test
    addition, subtraction, multiplication, division,
    equal, not equal, less than, less than or equal to,
    greater thangreater than or equal to
"""

import unittest
from HW03_Nidhi_Chovatiya import Fraction

class TestFraction(unittest.TestCase):
    """ Test the Fraction class """

    def test_init(self) -> None:
        """ To check that the numerator and denominator are set properly """
        f: Fraction = Fraction(7.0, 8.0)
        self.assertEqual(f.num, 7.0)
        self.assertEqual(f.denom, 8.0)

    def test_init_exception(self) -> None:
        """ To check that when denominator is zero, ZeroDivisionError is raised """
        with self.assertRaises(ZeroDivisionError):
            # trying to create denomiator = 0, which raise a ZeroDivisionError
            Fraction(7.0, 0.0)
        with self.assertRaises(ZeroDivisionError):
            Fraction(5.0,0.0)/Fraction(6.0,5.0)
        with self.assertRaises(TypeError):
            # input is not string raise a type error
            Fraction('a', 2.0) 

    def test_str(self) -> None:
        """ To check that the __str__ function works properly """
        f: Fraction = Fraction(7.0, 8.0)
        self.assertEqual(str(f), "7.0/8.0")

    def test_add(self) -> None:
        """ To check the Fraction addition """
        f78: Fraction = Fraction(7.0, 8.0)
        f19: Fraction = Fraction(1.0, 9.0)
        self.assertEqual(f78 + f19, Fraction(71.0, 72.0))
        # f78 should not have changed
        self.assertEqual(f78, Fraction(7.0, 8.0))  

    def test_add_more_than_2(self) -> None:
        """ To check the Fraction addition with more than two operands """
        f72: Fraction = Fraction(7.0, 2.0)
        f15: Fraction = Fraction(1.0, 5.0)
        f23: Fraction = Fraction(2.0, 3.0)
        self.assertTrue(f72 + f15 + f23 == Fraction(131.0, 30.0))

    def test_sub(self) -> None:
        """ To check Fraction substraction """
        f25: Fraction = Fraction(2.0, 5.0)
        f13: Fraction = Fraction(1.0, 3.0)
        self.assertEqual(f25 - f13, Fraction(1.0, 15.0))
        # f25 should not have changed
        self.assertEqual(f25, Fraction(2.0, 5.0))  

    def test_sub_more_than_2(self) -> None:
        """ To check Fraction substraction with more than two operands """
        f41: Fraction = Fraction(4.0, 1.0)
        f55: Fraction = Fraction(5.0, 5.0)
        f32: Fraction = Fraction(3.0, 2.0)
        self.assertTrue(f41 - f55 - f32 == Fraction(3.0, 2.0))

    def test_mul(self) -> None:
        """ To check the Fraction multiplication """
        f78: Fraction = Fraction(7.0, 8.0)
        f109: Fraction = Fraction(10.0, 9.0)
        self.assertEqual(f78 * f109, Fraction(35.0, 36.0))
        # f78 should not have changed
        self.assertEqual(f78, Fraction(7.0, 8.0))  

    def test_mul_more_than_2(self) -> None:
        """ To check the Fraction multiplication with more than two operands """
        f72: Fraction = Fraction(7.0, 2.0)
        f15: Fraction = Fraction(1.0, 5.0)
        f23: Fraction = Fraction(2.0, 3.0)
        self.assertTrue(f72 * f15 * f23 == Fraction(7.0, 15.0))

    def test_truediv(self) -> None:
        """ To check the Fraction division """
        f78: Fraction = Fraction(7.0, 8.0)
        f910: Fraction = Fraction(9.0, 10.0)
        self.assertEqual(f78 / f910, Fraction(35.0, 36.0))
        # f78 should not have changed
        self.assertEqual(f78, Fraction(7.0, 8.0))  

    def test_truediv_more_than_2(self) -> None:
        """ To check the Fraction division with more than two operands """
        f72: Fraction = Fraction(7.0, 2.0)
        f15: Fraction = Fraction(1.0, 5.0)
        f23: Fraction = Fraction(2.0, 3.0)
        self.assertTrue(f72 / f15 / f23 == Fraction(105.0, 4.0))

    def test_second_fraction_zerodivision(self) -> None:
        """ when the second Fraction's result is 0, ZeroDivisionError is raised  """
        with self.assertRaises(ZeroDivisionError):
            f78: Fraction = Fraction(7.0, 8.0)
            # nominator is 0, no error will be raised
            # but nominator of f05(second fraction) will be the denominator of f78(first fractiom)
            f05: Fraction = Fraction(0.0, 5.0)  
            # Due to dominator = zero, result will raise a ZeroDivisionError                                
            result = f78 / f05 

    def test_eq(self) -> None:
        """ To check the Fraction equality """
        f78: Fraction = Fraction(7.0, 8.0)
        f23: Fraction = Fraction(2.0, 3.0)
        f1518: Fraction = Fraction(15.0, 18.0)
        f1012: Fraction = Fraction(10.0, 12.0)

        self.assertEqual(f78 == f23, False)
        self.assertEqual(f1518 == f1012, True)

    def test_gt(self) -> None:
        """ To check the __gt__ function """
        f32: Fraction = Fraction(3.0, 2.0)
        f33: Fraction = Fraction(3.0, 3.0)
        f14: Fraction = Fraction(1.0, 4.0)
        f34: Fraction = Fraction(3.0, 4.0)
        fm13: Fraction = Fraction(-1.0, 3.0)

        self.assertEqual(f32 > f33, True)
        self.assertEqual(f14 > f34, False)
        # Test for negative number
        self.assertEqual(fm13 > f14, False)

    def test_ge(self) -> None:
        """ To check the __ge__ function """
        f32: Fraction = Fraction(3.0, 2.0)
        f33: Fraction = Fraction(3.0, 3.0)
        f25: Fraction = Fraction(2.0, 5.0)
        f14: Fraction = Fraction(1.0, 4.0)
        fm13: Fraction = Fraction(-1.0, 3.0)

        self.assertEqual(f33 >= f32, False)
        self.assertEqual(f25 >= f14, True)
        self.assertEqual(f25 >= f25, True)
        # Test for negative number
        self.assertEqual(fm13 >= f14, False)


    def test_lt(self) -> None:
        """ To check the __lt__ funcion """
        f32: Fraction = Fraction(3.0, 2.0)
        f33: Fraction = Fraction(3.0, 3.0)
        f14: Fraction = Fraction(1.0, 4.0)
        f34: Fraction = Fraction(3.0, 4.0)
        fm13: Fraction = Fraction(-1.0, 3.0)

        self.assertEqual(f32 < f33, False)
        self.assertEqual(f14 < f34, True)
        # Test for negative number
        self.assertEqual(fm13 < f14, True)

    def test_le(self) -> None:
        """ To check the __le__ function """
        f32: Fraction = Fraction(3.0, 2.0)
        f33: Fraction = Fraction(3.0, 3.0)
        f25: Fraction = Fraction(2.0, 5.0)
        f14: Fraction = Fraction(1.0, 4.0)
        fm13: Fraction = Fraction(-1.0, 3.0)

        self.assertEqual(f33 <= f32, True)
        self.assertEqual(f25 <= f14, False)
        self.assertEqual(f25 <= f25, True)
        # Test for negative number
        self.assertEqual(fm13 <= f14, True)


    def test_ne(self) -> None:
        """ To check the Fraction Inequality """
        f78: Fraction = Fraction(7.0, 8.0)
        f23: Fraction = Fraction(2.0, 3.0)
        f1518: Fraction = Fraction(15.0, 18.0)
        f1012: Fraction = Fraction(10.0, 12.0)

        self.assertEqual(f78 != f23, True)
        self.assertEqual(f1518 != f1012, False)

    def test_simplify(self) -> None:
        """ To check the simplify() function works properly"""
        self.assertTrue(str(Fraction(7.0, 9.0).simplify()) == str(Fraction(7.0, 9.0)))
        self.assertTrue(str(Fraction(9.0, 12.0).simplify()) == str(Fraction(3.0, 4.0)))
        self.assertTrue(str(Fraction(8.0, 32.0).simplify()) == str(Fraction(1.0, 4.0)))


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)