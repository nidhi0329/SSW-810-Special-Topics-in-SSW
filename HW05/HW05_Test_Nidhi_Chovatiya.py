""" Test implementation class of the study
    which focuses on string methods, slices,
    working with files, and automated testing
    author: Nidhi Chovatiya
    CWID: 10457344
"""

import unittest
from typing import List
from HW05_Nidhi_Chovatiya import reverse, substring, find_second, get_lines


class ReverseTest(unittest.TestCase):
    """ Test class of the methods """

    def test_reverse(self) -> None:
        """ testing reverse """
        self.assertTrue(reverse("Hello") == "olleH")
        self.assertTrue(reverse("abc") == "cba")
        self.assertTrue(reverse("nidhi") == "ihdin")

    def test_substring(self) -> None:
        """ testing substring """
        self.assertEqual(substring("Ni", "Nidhi"), 0)
        self.assertEqual(substring("idhi", "Nidhi"), 1)
        self.assertEqual(substring("", "Nidhi"), -1)
        self.assertEqual(substring("xyz", "abcxyz"), 3)

    def test_find_second(self) -> None:
        """ testing find_second """
        self.assertTrue(find_second("iss", "Mississippi") == 4)
        self.assertTrue(find_second("abba", "abbabba") == 3)
        self.assertEqual(find_second("", "Hello"), -1)

    def test_get_lines(self) -> None:
        """ testing get_lines """
        file_path = "C:/Users/Nidhi/Desktop/SEM3/810/HW05/test_file.txt"

        result: List[str] = list(get_lines(file_path))
        expect: List[str] = ['<line0>', '<line1>', '<line2>', '<line3.1 line3.2 line3.3>',
                             '<line4.1 line4.2>', '<line5>', '<line6>']

        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
