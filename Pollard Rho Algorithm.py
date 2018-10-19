# primitive code for Pollard Rho

from random import *
from math import *
from time import *

########################################################################################################################

def poly_eval(X, N):
    # evaluates the polynomial at X and reduces mod(N)

    # evaluate at f(X)
    val = X ** 2 + 1

    # reduce f(X) mod(N)
    red_val = val % N

    return red_val

########################################################################################################################

def pollard(N):
    greatest_div = 1

    while greatest_div == 1:
        # set initial condition for cycle of polynomial evaluations
        s_0 = randint(1, N - 1)
        t_0 = randint(1, N - 1)

        # compute f(X) mod(N)
        eval1 = poly_eval(s_0, N)
        eval2 = poly_eval(t_0, N)

        # compute the gcd
        greatest_div = gcd(eval1 - eval2, N)

        factor = greatest_div

        # EVENTUALLY DELETE THIS LINE
        # print("This is f(X):" , eval1)
        # print("This is f(Y):" , eval2)
        # print("This is the gcd( f(x) - f(y) ," , N , " ):" , factor)
        # print()

    return factor

########################################################################################################################

def main():
    number = 1

    while number != 0:

        number = int(input('Enter a number to factor or "0" to quit: '))

        if number != 0:

            print()

            total_time = 0

            # start clock
            initial_time = process_time()

            # factor the number
            factor1 = pollard(number)

            # NEED TO MAKE SURE factor!=number
            if factor1 == number:
                factor1 = pollard(number)

            # get other factor
            factor2 = int(number / factor1)

            print("The factors of", number, "are", factor1, "and", factor2)

            # end clock
            elapsed_time = process_time() - initial_time

            print("This took", elapsed_time, "seconds to calculate.")
            print()


main()