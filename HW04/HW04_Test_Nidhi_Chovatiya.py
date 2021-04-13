"""
@author: Nidhi Chovatiya
CWID : 10457344
    practice iterating over lists, ranges, and strings using for and while loops
"""

import random
import unittest
from typing import Iterator, List, Tuple
from HW04_Nidhi_Chovatiya import count_vowels, last_occurrence, my_enumerate

# PART 1
    
class CountVowelsTest(unittest.TestCase):
    
    def test_count_vowels(self) -> None:
        """ 
            testing count vowels 
        """
        # Count the vowels in given string, which is 3
        self.assertEqual(count_vowels('HeLlo wOrld'), 3)
        # Count the vowels in given string, which is 8 not 2
        self.assertNotEqual(count_vowels('SofTwaRE EngineEring'), 2)
        # Count the vowels in given string, which is 0
        self.assertEqual(count_vowels('sssshhhhhh'), 0)
                
# PART 2
    
class LastOccurrenceTest(unittest.TestCase):

    def test_last_occurrence(self) -> None:
        """ 
            testing last_occurrence 
        """
        # To check the last occurrence for 33, which is 4
        self.assertEqual(last_occurrence(33 , [22, 11, 33, 43, 33]), 4)
        # To check the last occurrence for i, which is 8
        self.assertEqual(last_occurrence("i", "Engineering"), 8)
        # Return None if the character is not in the string
        self.assertEqual(last_occurrence("1", "Engineering"), None)
        # To check the last occurrence for "Lotus", which is 4
        self.assertEqual(last_occurrence("Lotus", ["Rose", "Lotus", "Sunflower", "Rose", "Lotus"]), 4)
        # To check the last occurence for e, which is 6
        self.assertEqual(last_occurrence("e", "Engineering"), 6)
        # To check the last occurrence for p, which is 2
        self.assertEqual(last_occurrence('p', 'apple'), 2)
        # To check the last occurrence for r
        self.assertNotEqual(last_occurrence("r", "Engineering"), 5)
        # Return None if the woed is not in the given sentance
        self.assertEqual(last_occurrence("Test", "Exam is not today"), None)

# PART 4

class EnumerateTest(unittest.TestCase):

    def test_enumerate_list(self) -> None:
        """ 
            test my_enumerate by storing the results in a list 
        """
        string1: str = list(my_enumerate([0, 1, 2, 3, 4]))
        string2: str = list(enumerate([0, 1, 2, 3, 4]))
        # given strings are equal
        self.assertEqual(string1, string2)               
        string3: str = list(my_enumerate("Nidhi"))
        string4: str = list(enumerate("Chovatiya"))
        # given strings are not equal 
        self.assertNotEqual(string3, string4)           

        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)