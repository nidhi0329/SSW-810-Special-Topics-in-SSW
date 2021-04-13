"""A study focuses on Python Containers
    author: Nidhi Chovatiya
    CWID : 10457344
"""

from typing import DefaultDict, List, Tuple
from collections import defaultdict, Counter


def anagrams_lst(str1: str, str2: str) -> bool:
    """ returns True if str1 and str2 are anagrams, False if not """
    if not type(str1) is str or not type(str2) is str:
        raise TypeError
    s1: str = ''.join(sorted(list(str1.lower()))).lstrip()
    s2: str = ''.join(sorted(list(str2.lower()))).lstrip()
    if s1 != s2:
        return False
    else:
        return True


def anagrams_dd(str1: str, str2: str) -> bool:
    """ returns True if str1 and str2 are anagrams, False if not """
    if not type(str1) is str or not type(str2) is str:
        raise TypeError
    default_dict: DefaultDict[str, int] = defaultdict(int)

    for char in ''.join(sorted(str1.lower())).lstrip():
        default_dict[char] += 1

    for char in ''.join(sorted(str2.lower())).lstrip():
        if char in default_dict:
            default_dict[char] -= 1
        else:
            return False
    # if any of the value is not 0, return False, else return True.
    return not any(default_dict.values())


def anagrams_cntr(str1: str, str2: str) -> bool:
    """ returns True if str1 and str2 are anagrams, False if not """
    if not type(str1) is str or not type(str2) is str:
        raise TypeError
    s1: str = ''.join(sorted(str1.lower())).lstrip()
    s2: str = ''.join(sorted(str2.lower())).lstrip()
    if Counter(s1) != Counter(s2):
        return False
    else:
        return True


def covers_alphabet(sentence: str) -> bool:
    """ returns True if sentence includes at least
        one instance of every character in the alphabet or False"""
    if not type(sentence) is str:
        raise TypeError
    # This function is going to cover the alphabets
    s1: str = "abcdefghijklmnopqrstuvwxyz"
    s2: str = sentence.lower()
    if set(s2) >= set(s1):
        return True
    else:
        return False


def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
    """ returns a summary of the weblogs with each distinct site
        and a sorted list of names of distinct people who visited that site """
    default_dict: DefaultDict[str, List[str]] = defaultdict(list)

    for user, site in set(weblogs):
        if len(weblogs) != Tuple:
            raise ValueError
        # create a dictionary {site: [users]}
        default_dict[site].append(user)

    # return alphabetized list
    return [(key, sorted(default_dict[key])) for key in sorted(default_dict)]


if __name__ == '__main__':
    main()
