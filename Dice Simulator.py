# this program simulates rolling dice by letting the user choose the number of dice to be rolled and how many sides are on the dice

# June 18th, 2018

from random import randint

########################################################################################################################

def convert(num_d_num):

    # this function takes in the input [string] from the user that should be of the form number_"d"_number and returns
    # a two-element list (both elements of the list should be integers)

    # split the string input with the delimiter "d"
    split_input = num_d_num.split('d')

    # convert the elements of the list into integers

    #initialize the index counter
    index = 0

    # use a for loop to travers the list
    for element in split_input:

        # convert element in index position to integer
        split_input[index] = int(element)

        # add to index counter
        index += 1

    # returm the list of integers
    return split_input

########################################################################################################################

def simulator(dice_list):

    # this function takes in a two-element list [x , y] (each list == number of dice, number of sides) and returns random
    # integers (these are the result of the "dice rolls")

    # initialize a result list to store the simulated rolls
    results = []

    # use a for loop that iterates x times
    for i in range(dice_list[0]):

        # simulate a dice roll and append it to the result list
        roll = randint(1 , dice_list[1])
        results.append(roll)

    # return the list of results
    return results



########################################################################################################################

def main():

    # use a while loop to keep program open until user wants to close it
    keep_going = True

    while keep_going:

        # indicate how to exit the program to the user
        print("To exit this program, enter 'done'.")

        # ask user for input of number of dice and how many sides , e.g. 3d6 == three six-sided dice
        die = input("How many dice [x] and how many sides [y] are on the dice (enter as x_'d'_y):")

        # test if user entered 'done'
        if die == 'done':
            keep_going = False

        # this path executes if the user DID NOT want to exit the program
        else:
            print("\n\n\n")

            # call function that reads in input and turns it into list of tuples (?)
            die_list = convert(die)

            # call function that takes list of tuples and simulates dice rolls
            results = simulator(die_list)

            # print the results and explain what the configuration of the dice being rolled
            print('Results:' , results , '\n\n\n')


########################################################################################################################

main()