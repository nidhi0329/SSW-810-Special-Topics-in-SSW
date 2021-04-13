""" A study focuses on string methods, slices,
    working with files, and automated testing
    author: Nidhi Chovatiya
    CWID: 10457344
"""

from typing import List, Iterator, IO


def reverse(string: str) -> str:
    """ Takes a string as an argument and
        returns a new string which is the reverse of the argument
    """

    reverse_string: str = ""
    string_lenght: int = len(string)

    # run the loop in backwards and add each letter to the new string
    for index in range(string_lenght-1, -1, -1):
        reverse_string += string[index]

    # return the reversed string
    return reverse_string


def substring(target: str, string: str) -> int:
    """ A substring function that is similar to Python’s string.find(target) method that returns
        the offset from the beginning of  string "string" where target occurs in "string"
    """

    if not type(string) is str and not type(target) is str:
        raise TypeError

    string_lenght: int = len(string)
    target_lenght: int = len(target)

    for index in range(string_lenght - target_lenght + 1):
        if target_lenght == 0 or string_lenght == 0:
            return -1
        else:
            # create a new substring which will be compared with the target
            current: str = string[index: index + target_lenght]

            # if equal then return the current index
            if current == target:
                return index

    # if could not find any substring then return -1
    return -1


def find_second(target: str, string: str) -> int:
    """ Return the offset of the second occurrence of target in string.
        Return -1 if target does not occur twice in string
    """
    if not type(string) is str and not type(target) is str:
        raise TypeError

    string_lenght: int = len(string)
    target_lenght: int = len(target)

    for index in range(string_lenght - target_lenght + 1):
        # return - if target or string is empty
        if target_lenght == 0 or string_lenght == 0:
            return -1
        else:
            # find first occurence of the target string
            index: int = string.find(target)
            # find second occurence of the target string
            index = string.find(target, index+1)

            # return the index if second occurence of the target string is found otherwise it will returns -1
            return index

    # return -1


def get_lines(path: str) -> Iterator[str]:
    """ Opens a file for reading and yields one line from the file at a time """

    # add lines to a list to work on
    lines: List[str] = []

    # opening the file
    try:
        file_path: IO = open(path, "r")
    except:
        raise FileNotFoundError
    else:
        with file_path:
            for line in file_path:
                lines.append(line)

    # lines starting with '#' will be deleted
    delete_list: List[int] = []

    index: int = 0

    while index < len(lines):
        # combining all the continuous lines
        while lines[index].endswith("\\\n"):

            # add the next line to the current line
            lines[index] = lines[index].strip("\\\n") + lines[index + 1]

            # remove the added(next) line
            lines.pop(index + 1)

        # remove the next line '\n'
        if lines[index].endswith("\n"):
            lines[index] = lines[index][:lines[index].find("\n")]

        # if the line is a comment add it's index to the removed list
        if lines[index].startswith("#"):
            delete_list.append(index)

        # if there is an inline comments remove comment
        if lines[index].find("#") != -1:
            lines[index] = lines[index][:lines[index].find("#")]

        index += 1

    # delete the comment lines
    for i in delete_list[::-1]:
        lines.pop(i)

    for line in lines:
        yield line


if __name__ == '__main__':
    main()
