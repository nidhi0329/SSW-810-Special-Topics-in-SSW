""" 
@author: Nidhi Chovatiya
CWID : 10457344
    Implement a class for fractions that supports
    addition, subtraction, multiplication, division and check if
    equal, not equal, less than, less than or equal to,
    greater than, greater than or equal to
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
        if not type(num) is float or not type(denom) is float:
            raise TypeError
        self.num: float = num
        self.denom: float = denom

    def __str__(self) -> str:
        """ return a String to display fractions """
        return f"{float(self.num)}/{float(self.denom)}"

    def __add__(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        plus_num: float = (self.num * other.denom) +  (other.num * self.denom)
        plus_denom: float = self.denom * other.denom
        plus_fraction: Fraction = Fraction(plus_num, plus_denom)

        return plus_fraction.simplify()

    def __sub__(self, other: "Fraction") -> "Fraction":
        """ subtract two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        minus_num: float = (self.num * other.denom) - (other.num * self.denom)
        minus_denom: float = self.denom * other.denom
        minus_fraction: Fraction = Fraction(minus_num, minus_denom)

        return minus_fraction.simplify()

    def __mul__(self, other: "Fraction") -> "Fraction":
        """ Multiply two fractions using simplest approach
            Calculate new numerator and denominator and return new Fraction
        """
        times_num: float = self.num * other.num
        times_denom: float = self.denom * other.denom
        times_fraction: Fraction = Fraction(times_num, times_denom)

        return times_fraction.simplify()

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """ Add two fractions using simplest approach.
            Calculate new numerator and denominator and return new Fraction
        """
        divide_num: float = self.num * other.denom
        divide_denom: float = self.denom * other.num
        divide_fraction: Fraction = Fraction(divide_num, divide_denom)

        return divide_fraction.simplify()

    def __eq__(self, other: "Fraction") -> bool:
        """ if the two fractions are equivalent
            then return True
            otherwise return False
        """
        LHS: float = self.num * other.denom
        RHS: float = self.denom * other.num

        if LHS == RHS:
            #the fractions are equal
            return True
        else:
            # the fractions are not equal
            return False

    def __gt__(self, other: "Fraction") -> bool:
        """ if the first fraction is greater than the second fraction 
            then return True 
            otherwise return False 
        """
        f1: float = self.num / self.denom
        f2: float = other.num / other.denom

        if f1 > f2:
            return True
        else:
            return False

    def __ge__(self, other: "Fraction") -> bool:
        """ if the first fraction is greater than or equal to the second fraction 
            then return True 
            otherwise return False 
        """
        f1: float = self.num / self.denom
        f2: float = other.num / other.denom

        if f1 >= f2:
            return True
        else:
            return False 

    def __lt__(self, other: "Fraction") -> bool:
        """ if the first fraction is less than the second fraction 
            then return True 
            otherwise return False  
        """
        f1: float = self.num / self.denom
        f2: float = other.num / other.denom

        if f1 < f2:
            return True
        else:
            return False

    def __le__(self, other: "Fraction") -> bool:
        """ if the first fraction is less than or equal to the second fraction 
            then return True 
            otherwise return False 
        """
        f1: float = self.num / self.denom
        f2: float = other.num / other.denom

        if f1 <= f2:
            return True
        else:
            return False

    def __ne__(self, other: "Fraction") -> bool:
        """ if the two fractions are not equivalent
            then return True 
            otherwise return False 
        """
        LHS: float = self.num * other.denom
        RHS: float = self.denom * other.num

        if LHS == RHS:
            #the fractions are equal
            return False
        else:
            # the fractions are not equal
            return True

    def simplify(self) -> "Fraction":
        """ Find the Greatest Common Factor to simplify the fraction
            and then dividing the number and denominator.
        """
        # a function to find the gcd
        def gcd(n1, d1): 
            while d1 != 0:
                (n1, d1) = (d1, n1%d1)
            return n1

        temp: int = gcd(int(self.num), int(self.denom))
        new: int = min(abs(int(self.num)), abs(int(self.denom)))

        for value in range(new, 2, -1):
            if value % temp:
                return Fraction(float(self.num / temp), float(self.denom / temp))

        return Fraction(float(self.num), float(self.denom))


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

# def compute(f1: Fraction, operator: str, f2: Fraction) -> None:
#     """ Given two fractions and an operator, return the result
#         of applying the operator to the two fractions
#     """

#     #define the type of the result
#     output: Optional[Union[Fraction, bool]] 
#     #print the result
#     result: bool = True 

#     if operator == '+':
#         output = f1 + f2
#     elif operator == "-":
#         output = f1 - f2
#     elif operator == "*":
#         output = f1 * f2
#     elif operator == "/":
#         output = f1 / f2
#     elif operator == "==":
#         output = f1 == f2
#     elif operator == ">":
#         output = f1 > f2
#     elif operator == ">=":
#         output = f1 >= f2
#     elif operator == "<":
#         output = f1 < f2
#     elif operator == "<=":
#         output = f1 <= f2
#     elif operator == "!=":
#         output = f1 != f2
#     else:
#         print(f"Oops! '{operator}' is not valid operator")
#         # invalid operator. So, output is not displayed
#         result = False 

#     if result:
#         print(f"{f1} {operator} {f2} = {output}")


def main() -> None:
    """ Fraction calculations """
    print('Welcome to the fraction calculator!')
    f1: Fraction = get_fraction(1)
    operator: str = input("Enter a valid operator to perform operation (+, -, *, /, ==, !=, <, <=, >, >=): ")
    f2: Fraction = get_fraction(2)

    try:
        compute(f1, operator, f2)
    except ZeroDivisionError:
        print("Oops! Error due to Zero Division")


if __name__ == '__main__':
    # test_suite()
    main()
