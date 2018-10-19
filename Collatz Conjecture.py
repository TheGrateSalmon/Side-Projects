# Collatz Conjecture (3n+1)

# performs the 3n+1 algorithm for any positive integer

from time import *


def main():
    number = int(input('Input any positive integer or "0" to quit: '))

    while number < 0:
        number = int(input('That is not a valid input. Please input any positive integer or "0" to quit: '))

    step = 0

    # if number = 0, exits program
    while number != 0:

        while number > 1:

            initial_time = process_time()

            step += 1

            # number is even
            if number % 2 == 0:
                number = number // 2

            # number is odd
            else:
                number = 3 * number + 1

            elapsed_time = process_time() - initial_time

        print("This number has a total stopping time of ", step, " and took ", elapsed_time, " seconds to calculate.\n",
              sep="")

        number = int(input('Input any positive integer or "0" to quit: '))

        # reinitialize step
        step = 0


main()