# this program computes the sum of the GCD's of a set of numbers

# more info can be found here:   https://projecteuler.net/problem=625

from math import *

########################################################################################################################

def inner(j):
    # this computes the inner sum of the expression (sum of the GCD's)

    partial_total = 0

    for i in range(1 , j+1):

        partial_total += (gcd(i , j) % 998244353)

    return partial_total

########################################################################################################################

def main():

    # ask user for a positive integer input
    N = abs(int(input("Enter any postive integer: "))) % 998244353

    # inititalize the total for an accumulator
    total = 0

    for i in range(1 , N+1):

        total += inner(i)
        total = total % 998244353

    print()
    print("The total is" , total)

########################################################################################################################

main()