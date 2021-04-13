""" A study focuses on date operations and working with files (prettytable)
    author: Nidhi Chovatiya
    CWID: 10457344
"""

from datetime import datetime, timedelta
from typing import Iterator, Tuple, Dict, List
import os
from prettytable import PrettyTable


def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """ return a tuple with
        the date three days after Feb 27, 2020
        the date three days after Feb 27, 2019
        HOw many days passed between Feb 1, 2019 and sept 30, 2019
        Code segment demonstrating expected return values. 
    """

    dt_02272020: datetime = datetime(2020, 2, 27)
    delta1: timedelta = timedelta(days=3)
    dt1: datetime = dt_02272020 + delta1

    dt_02272019: datetime = datetime(2019, 2, 27)
    delta2: timedelta = timedelta(days=3)
    dt2: datetime = dt_02272019 + delta2

    dt_09302019: datetime = datetime(2019, 9, 30)
    dt_02012019: datetime = datetime(2019, 2, 1)
    delta3: timedelta = dt_09302019 - dt_02012019

    return dt1, dt2, delta3.days


def file_reader(path: str, fields: int, sep: str = ',', header: bool = False) -> Iterator[List[str]]:
    """In this function, we will implement a generator that will yield
    new line of a file on call of next

    Args:
        path (str): File Path
        fields (int): fields
        sep (str, optional): Separator. Defaults to ','.
        header (bool, optional): Defaults to False.

    Yields:
        Iterator[Tuple[str]]
    """
    try:
        fp: IO = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Cannot open file at {path} ")
    else:
        with fp:
            line_number: int = 0
            for line in fp:
                row: List[str] = line.strip().split(sep)
                line_number += 1
                if len(row) != fields:
                    fp.close()
                    raise ValueError(
                        f"File {path} at line {line_number} has  {len(row)} items, whereas the \
                        expected items where {fields} ")
                if header is False:
                    yield row
                else:
                    header = False


class FileAnalyzer:
    """ a class that given a directory name, searches that directory
        for Python files and calculates a summary of the file """

    def __init__(self, directory: str) -> None:
        """ store the directory and files summary """
        if not os.path.exists(directory):
            raise FileNotFoundError(
                f"The specified directory ‘{directory}’ is not found")

        self.directory: str = directory
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        # summarize the python files data
        self.analyze_files()

    def analyze_files(self) -> None:
        """ analyze the file """
        for file in os.listdir(self.directory):
            if file.endswith(".py"):
                try:
                    py_file = open(os.path.join(self.directory, file), "r")
                except FileNotFoundError:
                    raise FileNotFoundError(
                        f"File {py_file} is not found or can not be opened")

                # close file after opening
                with py_file:
                    class_count: int = 0
                    function_count: int = 0
                    line_count: int = 0
                    char_count: int = 0

                    # calculate values for the file
                    for line in py_file:
                        if line.strip().startswith("class "):
                            class_count += 1
                        elif line.strip().startswith("def "):
                            function_count += 1

                        line_count += 1
                        char_count += len(line)

                    self.files_summary[str(os.path.join(self.directory, file))] = {
                        "class": class_count,
                        "function": function_count,
                        "line": line_count,
                        "char": char_count
                    }

    def pretty_print(self) -> None:
        """ prettify the data """
        result: PrettyTable = PrettyTable()
        result.field_names = ["File Name", "Classes",
                              "Functions", "Lines", "Characters"]
        # add rows to the table
        for i, j in self.files_summary.items():
            # key(file) and values
            result.add_row([i] + list(j.values()))

        print(result)
