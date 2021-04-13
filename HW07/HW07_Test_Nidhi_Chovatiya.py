""" Test implementation class of the study
    which focuses on Python Containers
    author: Nidhi Chovatiya
    CWID : 10457344
"""

import unittest

from typing import List, Tuple
from HW07_Nidhi_Chovatiya import anagrams_lst, anagrams_dd, anagrams_cntr, covers_alphabet, web_analyzer


class ListTest(unittest.TestCase):
    """ Test class of the methods """

    def test_anagrams_lst(self) -> None:
        """ testing anagram list """
        self.assertTrue(anagrams_lst("School Master", "The classroom"))
        self.assertTrue(anagrams_lst("Funeral", "Real fun"))
        self.assertTrue(anagrams_lst("nidhi", "NIDHI"))
        self.assertFalse(anagrams_lst("python", ""))

    def test_anagrams_dd(self) -> None:
        """ testing anagram defaultdict """
        self.assertTrue(anagrams_dd("School Master", "The classroom"))
        self.assertTrue(anagrams_dd("Funeral", "Real fun"))
        self.assertTrue(anagrams_dd("nidhi", "NIDHI"))
        self.assertFalse(anagrams_dd("python", ""))

    def test_anagrams_cntr(self) -> None:
        """ testing anagram counter """
        self.assertTrue(anagrams_cntr("School Master", "The classroom"))
        self.assertTrue(anagrams_cntr("nidhi", "NIDHI"))
        self.assertFalse(anagrams_cntr("python", ""))
        self.assertTrue(anagrams_cntr("Funeral", "Real fun"))

    def test_covers_alphabet(self) -> None:
        """ testing covers alphabet """
        self.assertTrue(covers_alphabet("aabbcdefghijklmnopqrstuvwxyzzabc"))
        self.assertTrue(covers_alphabet(
            "The quick, brown, fox; jumps over the lazy dog!"))
        self.assertTrue(covers_alphabet(
            "We promptly judged antique ivory buckles for the next prize"))
        self.assertFalse(covers_alphabet("abcdehjuidnrhsm"))
        self.assertFalse(covers_alphabet("123456789245667"))
        self.assertTrue(covers_alphabet("abcdefghijklmnopqrstuvwxyz"))
        self.assertTrue(covers_alphabet("AbCdefghiJklomnopqrStuvwxyz"))

    def test_web_analyzer(self) -> None:
        """ testing web analyzer """
        weblogs: List[Tuple[str, str]] = [
            ('Nanda', 'google.com'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Maha', 'google.com'),
            ('Fei', 'python.org'), ('Nanda', 'python.org'),
            ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
            ('Maha', 'google.com'), ]
        # weblogs: List[Tuple[str, str]] = [
        #     ('Maha'),
        #     ('Fei', 'python.org'), ('google.com'),
        #     ('Nanda', 'python.org'), ('Nanda', 'python.org'),
        #     ('Fei'), ('Nanda', 'google.com'),
        #     ('Maha', 'google.com')]


        summary: List[Tuple[str, List[str]]] = [
            ('dzone.com', ['Fei']),
            ('google.com', ['Maha', 'Nanda']),
            ('python.org', ['Fei', 'Nanda']), ]

        self.assertEqual(web_analyzer(weblogs), summary)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
