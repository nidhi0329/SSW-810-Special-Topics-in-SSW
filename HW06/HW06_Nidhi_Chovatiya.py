""" A study focuses on list comprehension
    author: Nidhi Chovatiya
    CWID : 10457344
"""

from typing import Any, List, Optional


def list_copy(lst: List[Any]) -> List[Any]:
    """ Takes a list as a parameter and returns
        a copy of the list using a list comprehension
    """
    copy: List[Any] = [item for item in lst]

    # return the copied list
    return copy


def list_intersect(lst1: List[Any], lst2: List[Any]) -> List[Any]:
    """ takes two lists as  parameters and returns
        a new list with the values that are included in both lists
    """
    intersection: List[Any] = [item for item in lst1 if item in lst2]

    # return the intersection list
    return intersection


def list_difference(lst1: List[Any], lst2: List[Any]) -> List[Any]:
    """ takes two lists as  parameters and returns
        a new list with the values in list1 that are not included in list2
    """
    difference: List[Any] = [item for item in lst1 if item not in lst2]

    # return the difference
    return difference


def remove_vowels(string: str) -> str:
    """ a function that given a string, splits the string on whitespace into words
        and returns a new string that includes only the words that do NOT begin with vowels
    """
    """Remove the elements starting with vowels"""
    s1 = " ".join([word for word in string.split() if word[0] not in [
                  'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']])
    return s1


def check_pwd(password: str) -> bool:
    """start with digit, atleast two uppercase and atleast one lower case then only password is correct"""
    pw = (len(password) >= 4) and ((len([x for x in password if x.isupper()]) >= 2) and any(
        x.islower() for x in password) and (password[0].isdigit()))
    return pw


class Queue:
    def __init__(self) -> None:
        self.queue: List[str] = list()

    def addcustomer(self, name: str) -> None:
        """All customers in a list"""
        self.queue.append(name)

    def get_nextcustomer(self) -> Optional[str]:
        """served customers are to be removed"""
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def waitingcustomer(self) -> List[str]:
        """Waiting customerS"""
        return self.queue


class DonutQueue():
    """This class will serve vip customers first and then normal"""

    def __init__(self) -> None:
        self.vip_queue: Queue = Queue()
        self.standard_queue: Queue = Queue()

    def arrive(self, name: str, vip: bool) -> None:
        """order of arriving"""
        if vip:
            self.vip_queue.addcustomer(name)
        else:
            self.standard_queue.addcustomer(name)

    def next_customer(self) -> str:
        """decides the next customer to be served"""
        customer = self.vip_queue.get_nextcustomer()
        if customer is None:
            customer = self.standard_queue.get_nextcustomer()
        return customer

    def waitinglist(self) -> str:
        """waiting list and call waitingcustomer"""
        vippeople = self.vip_queue.waitingcustomer()
        standardpeople = self.standard_queue.waitingcustomer()
        everyone = vippeople + standardpeople
        """separeted by comma all the customers"""
        return ", ".join(everyone)


# excution starts from here
if __name__ == '__main__':
    main()
