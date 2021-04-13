"""
@author: Nidhi Chovatiya
CWID : 10457344
    practice iterating over lists, ranges, and strings using for and while loops
"""

import random
import unittest
from typing import Any, List, Optional, Sequence, Iterator

# PART 1

def count_vowels(s: str) -> int:
    ''' return the number of vowels in the string s '''
    # Convert string into lowercase
    String_lowercase = s.lower()
    # define counter(initial value is zero) which stores the number of vowel
    vowels : int = 0
    
    for i in String_lowercase:
        if i in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1  # if the char is vowel, increase the counter

    return vowels
        
# PART 2
    
def last_occurrence(target: Any, seq: Sequence[Any]) -> Optional[int]:
    ''' return the offset from 0 of the last occurrence of target in seq '''
    # trying to find the first occurrence
    try:
        Output: Optional[int] = seq.index(target)
    # cannot find any target in the sequence
    except ValueError:  
        return None

    # if one occurrence is found, continue to search until the last occurrence
    while True:  
        sub_seq: Sequence[Any] = seq[Output+1:]       # create a subsequence starting from the found index+1
                                                      # to search the target in the new sequence
        try:
            new_Output: int = sub_seq.index(target)   # if a new occurance is found
            Output += new_Output + 1                  # update the index
        except ValueError:                            # if cannot find any other target in the sequence
            break                                     # the last occurrence is already found, stop searching

    return Output
    
# PART 4
def my_enumerate(seq: Sequence[Any]) -> Iterator[Any]:
    """ emulate the behavior of Python's built in enumerate() function.
        For each call, return a tuple with the offset from 0 and the next item
    """
    for offset in range(len(seq)):
        yield offset, seq[offset]

if __name__ == '__main__':
    main()
    

