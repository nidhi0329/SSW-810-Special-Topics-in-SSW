# """ Test implementation class of the study which
#     focuses on date operations and working with files (prettytable)
#     author: Nidhi Chovatiya
#     CWID: 10457344
# """

import unittest
from datetime import datetime
from typing import List, Dict
from HW08_Nidhi_Chovatiya import date_arithmetic, file_reader, FileAnalyzer


class TestDateAndFile(unittest.TestCase):
    """ Test class of the methods """

    def test_date_arithmetic(self) -> None:
        """ testing date arithmetic """
        self.assertEqual(date_arithmetic(), (datetime(2020, 3, 1, 0, 0),
                                             datetime(2019, 3, 2, 0, 0),
                                             241))

    def test_file_reader(self) -> None:
        """
        In this function, we will test the file_reader() function
        """
        result = [['123', 'Jin He', 'Computer Science'],
                  ['234', 'Nanda Koka', 'Software Engineering'],
                  ['345', 'Benji Cai', 'Software Engineering']]
        # file have header
        self.assertTrue(
            list(file_reader('C:/Users/Nidhi/Desktop/SEM3/810/HW08/student_majors.txt', 3, '|', True)) == result)
        # file without header
        self.assertFalse(
            list(file_reader('C:/Users/Nidhi/Desktop/SEM3/810/HW08/student_majors.txt', 3, '|')) == result)
        # More than 3 datafield
        with self.assertRaises(ValueError):
            list(file_reader(
                'C:/Users/Nidhi/Desktop/SEM3/810/HW08/student_majors.txt', 4, '|', True))
        # file not found
        with self.assertRaises(FileNotFoundError):
            list(file_reader('abc.txt', 3, '|', True))

    def test_file_analyzer(self) -> None:
        """ testing file analyzer """
        with self.assertRaises(FileNotFoundError):
            # invalid directory
            f1 = FileAnalyzer("doesn't_exist")
            f1.pretty_print()

        f_analyzer: FileAnalyzer = FileAnalyzer(
            "C:/Users/Nidhi/Desktop/SEM3/810/HW08_test")  # valid directory
        expect: List[Dict[str, int]] = [{'class': 0, 'function': 0, 'line': 3, 'char': 57},
                                        {'class': 2, 'function': 4,
                                            'line': 25, 'char': 270},
                                        {'class': 0, 'function': 4,
                                            'line': 73, 'char': 2413},
                                        {'class': 0, 'function': 3, 'line': 60, 'char': 2065}]

        self.assertTrue(list(f_analyzer.files_summary.values()) == expect)

    def test_pretty_print(self) -> None:
        test = FileAnalyzer('C:/Users/Nidhi/Desktop/SEM3/810/HW08_test')
        test.pretty_print()


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
