""" Test implementation class of the study
    which focuses on list comprehension
    author: Nidhi Chovatiya
    CWID : 10457344
"""

import unittest

from HW06_Nidhi_Chovatiya import list_copy, list_intersect, list_difference, remove_vowels, check_pwd, DonutQueue
# from app import DonutQueue


class List_copy(unittest.TestCase):
    def test_list_copy(self) -> None:
        """test case for copy of list"""
        self.assertEqual(list_copy(['x', 'y', 'z']), ['x', 'y', 'z'])
        self.assertEqual(list_copy(['7', '8', '9']), ['7', '8', '9'])
        self.assertEqual(list_copy(['X', 'x', '1']), ['X', 'x', '1'])


class List_intersect(unittest.TestCase):
    def test_list_intersect(self) -> None:
        """test case for intersection of list"""
        self.assertEqual(list_intersect(
            ['x', 'y', 'z'], ['x', 'y', 'w']), ['x', 'y'])
        self.assertEqual(list_intersect(
            ['7', '4', '5'], ['7', '5', '8']), ['7', '5'])
        self.assertEqual(list_intersect(['a', 'b', 'c'], ['x', 'y', 'z']), [])
        self.assertEqual(list_intersect([], ['A', 'B', 'C']), [])
        self.assertEqual(list_intersect(['1', '2', '3'], ['A', 'B', 'C']), [])
        self.assertEqual(list_intersect(
            ['1', 'a', '3'], ['4', 'a', '6']), ['a'])


class List_difference(unittest.TestCase):
    def test_list_difference(self) -> None:
        """test case for list difference"""
        self.assertEqual(list_difference(
            ['x', 'y', 'z'], ['x', 'y', 'w']), ['z'])
        self.assertEqual(list_difference(['5', '6', '7'], [
                         '4', '8', '9']), ['5', '6', '7'])
        self.assertEqual(list_difference(['a', 'b', 'c'], ['a', 'b', 'c']), [])
        self.assertEqual(list_difference([], ['a', 'b', 'c']), [])


class Remove_vowels(unittest.TestCase):
    def test_remove_vowels(self) -> None:
        """test case for removing vowels"""
        self.assertEqual(remove_vowels('An Orange'), '')
        self.assertEqual(remove_vowels('This is an Apple'), 'This')
        self.assertEqual(remove_vowels('Apple has red color'), 'has red color')
        self.assertEqual(remove_vowels(
            'pila pila pine pine pila pila'), 'pila pila pine pine pila pila')


class Check_pwd(unittest.TestCase):
    def test_check_password(self) -> None:
        """test case for checking password"""
        self.assertTrue(check_pwd('2AbhhE'))
        self.assertTrue(check_pwd('0hj454@6hBH'))
        self.assertTrue(check_pwd('1ja!2AB'))
        # less than 4
        self.assertFalse(check_pwd('4XY'))
        self.assertFalse(check_pwd('aa'))
        self.assertFalse(check_pwd(''))


class DonutQueueTest(unittest.TestCase):
    """test case for donut queue"""

    def test_queue(self) -> None:
        d1 = DonutQueue()
        self.assertIsNone(d1.next_customer())
        d1.arrive("Sujit", False)
        d1.arrive("Fei", False)
        d1.arrive("Prof JR", True)
        self.assertEqual(d1.waitinglist(), "Prof JR, Sujit, Fei")
        d1.arrive("Nanda", True)
        self.assertEqual(d1.waitinglist(), "Prof JR, Nanda, Sujit, Fei")
        self.assertEqual(d1.next_customer(), "Prof JR")
        self.assertEqual(d1.next_customer(), "Nanda")
        self.assertEqual(d1.next_customer(), "Sujit")
        self.assertEqual(d1.waitinglist(), "Fei")
        self.assertEqual(d1.next_customer(), "Fei")
        self.assertIsNone(d1.next_customer())


# start from here
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
