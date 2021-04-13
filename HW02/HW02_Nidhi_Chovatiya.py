""" 
@author: Nidhi Chovatiya
    Implement a class for fractions that supports
    addition, subtraction, multiplication, division
"""

class Fraction:
    """ Support addition, subtraction, multiplication, division of fractions
        with a simple algorithm
    """

    def __init__(self, num: float, denom: float) -> None:
        """ store num and denom
            Raise ZeroDivisionError on 0 denominator
        """
        if denom == 0.0:
            raise ZeroDivisionError

        self.num: float = num
        self.denom: float = denom

    def __str__(self) -> str:
        """ return a String to display fractions """
        return f"{self.num}/{self.denom}"

    def plus(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        plus_num: float = (self.num * other.denom) + (other.num * self.denom)
        plus_denom: float = self.denom * other.denom
        plus_fraction: Fraction = Fraction(plus_num, plus_denom)

        return plus_fraction

    def minus(self, other: "Fraction") -> "Fraction":
        """ subtract two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        minus_num: float = (self.num * other.denom) - (other.num * self.denom)
        minus_denom: float = self.denom * other.denom
        minus_fraction: Fraction = Fraction(minus_num, minus_denom)

        return minus_fraction

    def times(self, other: "Fraction") -> "Fraction":
        """ Multiply two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        times_num: float = self.num * other.num
        times_denom: float = self.denom * other.denom
        times_fraction: Fraction = Fraction(times_num, times_denom)

        return times_fraction

    def divide(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        divide_num: float = self.num * other.denom
        divide_denom: float = self.denom * other.num
        divide_fraction: Fraction = Fraction(divide_num, divide_denom)

        return divide_fraction

    def equal(self, other: "Fraction") -> bool:
        """ return True/False if the two fractions are equivalent """
        LHS: float = self.num * other.denom
        RHS: float = self.denom * other.num

        if LHS == RHS:
            #the fractions are equal
            return True
        else:
            # the fractions are not equal
            return False 


def test_suite() -> None:
    """ We'll see a better testing approach next week but here's a start.
        Note that each statement includes the result of the computation plus
        the expected answer to help to quickly identify if everything works properly.
    """
    f12: Fraction = Fraction(1, 2)
    f34: Fraction = Fraction(3, 4)
    f56: Fraction = Fraction(5, 6)
    f77: Fraction = Fraction(7, 7)
    f82: Fraction = Fraction(8, 2)
    f99: Fraction = Fraction(9, 9)
    f98: Fraction = Fraction(9, 8)
    f106: Fraction = Fraction(10, 6)
    f912: Fraction = Fraction(9, 12)

    print(f"{f12} + {f34} = {f12.plus(f34)} [10/8]")
    print(f"{f34} + {f56} + {f106} = {f34.plus(f56).plus(f106)} [468/144]")

    print(f"{f82} - {f77} = {f82.minus(f77)} [42/14]")
    print(f"{f82} - {f12} - {f34} = {f82.minus(f12).minus(f34)} [44/16]")

    print(f"{f98} * {f99} = {f98.times(f99)} [81/72]")
    print(f"{f82} * {f77} * {f12} = {f82.times(f77).times(f12)} [56/28]")

    print(f"{f82} / {f106} = {f82.divide(f106)} [48/20]")
    print(f"{f34} / {f56} / {f99} = {f34.divide(f56).divide(f99)} [162/180]")

    print(f"{f99} == {f98} is {f99.equal(f98)} [False]")
    print(f"{f34} == {f912} is {f34.equal(f912)} [True]")

def get_number(prompt: str) -> float:
    """ read and return a number from the user.
        Loop until the user provides a valid number.
    """
    while True:
        inp: str = input(prompt)
        try:
            return float(inp)
        except ValueError:
            print(f"Error: '{inp}' is not a number. Please try again...")


def get_fraction(count: int) -> Fraction:
    """ Ask the user for a numerator and denominator and return a valid Fraction """
    while True:
        num = get_number(f"Enter a numerator for Fraction {count}: ")

        while True:
            denom = get_number(f"Enter a denominator for Fraction {count}: ")
            if denom == 0:
                print("Denominator cannot be 0. Please enter another number.")
            else:
                break

        fraction: Fraction = Fraction(num, denom)
        return fraction

def compute(f1: Fraction, operator: str, f2: Fraction) -> None:
    """ Given two fractions and an operator, return the result
        of applying the operator to the two fractions
    """
    output: Fraction  
    result: bool = True 

    if operator == '+':
        output = f1.plus(f2)
    elif operator == "-":
        output = f1.minus(f2)
    elif operator == "*":
        output = f1.times(f2)
    elif operator == "/":
        output = f1.divide(f2)
    elif operator == "==":
        equality: bool = f1.equal(f2)
        print(f"{f1} {operator} {f2} = {equality}")
        result = False
    else:
        print(f"Oops! '{operator}' is not valid operator")
        # invalid operator. So, output is not displayed
        result = False 

    if result:
        print(f"{f1} {operator} {f2} = {output}")


def main() -> None:
    """ Fraction calculations """
    print('Welcome to the fraction calculator!')
    f1: Fraction = get_fraction(1)
    operator: str = input("Enter a valid operator to perform operation (+, -, *, /, ==): ")
    f2: Fraction = get_fraction(2)

    try:
        compute(f1, operator, f2)
    except ZeroDivisionError:
        print("Error due to Zero Division")


if __name__ == '__main__':
    test_suite()
    main()
