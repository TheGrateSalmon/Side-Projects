# this program calculates the sum of the even Fibonacci numbers for a given range

# more info can be found here:   https://projecteuler.net/problem=2

# June 21st, 2018

########################################################################################################################

def fibonacci(ceiling):

    # this function calculates the Fibonacci numbers in a given range and adds the even ones to a list

    # initialize the first numbers for the Fibonacci sequence
    f_1 = 1
    f_2 = 1
    f_3 = 2

    # initialize the list of even Fibonacci numbers
    evens = []

    # use a for loop to iterate to the nth Fibonacci number
    while f_3 < ceiling:

        # add the previous two terms
        f_3 = f_1 + f_2

        # test if even

        # f_3 is even
        if (f_3 % 2 ) == 0 and f_3 < ceiling:

            # append number to list of even Fibonacci numbers
            evens.append(f_3)

        # set new value for f_1 and f_2
        f_1 = f_2
        f_2 = f_3

    # return the last Fibonacci number
    return evens

########################################################################################################################

def main():

    # explain what the program does to the user and how to exit the program
    print("This program calculates the sum of the even Fibonacci numbers for a given range.")
    print("To exit this program, enter 'done'.\n")

    keep_going = True

    # use a while loop to keep the program running until the user wants to exit
    while keep_going:

        # ask user for range to use
        ceil = input("Enter a postive integer: ")

        # user wants to exit program
        if ceil == 'done':
            keep_going = False

        # user wants to continue with program
        else:

            # convert ceil to an integer
            ceil = int(ceil)

            # find the even numbers for the given range
            evens = fibonacci(ceil)

            # initialize the total
            total = 0

            # sum the even Fibonacci numbers together using a for loop
            for num in evens:

                # add num to the total
                total += num

            # print the sum of the even Fibonacci numbers and how many there were
            print("The sum of all of the even Fiboncci numbers under " , ceil , " is " , total , "." , sep='')
            print("The number of even Fibonacci numbers under " , ceil ," is " , len(evens) , "." , sep='')
            print("\n\n\n")

########################################################################################################################

main()