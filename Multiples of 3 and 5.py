# this prgoram determines the multiples of 3 and 5 below a given number and returns the total of these multiples and how many there are

# June 21st, 2018

########################################################################################################################

def multiples(ceiling):

    # this function determines the multiples of 3 and 5 below the "ceiling" number

    # checks the multiples of 3 first by using a range starting at 3 and incrementing by 3 until i >= ceiling and adds the results to a list, X
    # then checks the multiples of 5 by using a range staring at 5 and incrementing by 5 until i >= ceiling and adds the results to a list, Y
    # check for repetitions in results by comparing lists; append these to a new list Z and delete from lists X , Y

    # initialize lists for multiples
    mult_3 = []
    mult_5 = []
    mult_both = []

    # use while loops to run until num > ceiling

    # intialize num to 3 for use in checking for the multiples of 3
    num = 3

    # check for multiples of 3
    while num < ceiling:

        # append num to the list of multiples of 3
        mult_3.append(num)

        # increment num by 3
        num += 3

    # initialize num to 5 for use in checking for the multiples of 5
    num = 5

    # check for multiples of 5
    while num < ceiling:

        # append_num to the list of the multiples of 5
        mult_5.append(num)

        # increment num by 5
        num += 5

    # check intersection of mult_3 and mult_5 list

    # mult_3 is nonempty
    if mult_3:

        # both mult_3 and mult_5 are nonempty
        if mult_5:

            # check intersection
            for element in mult_5:

                if element in mult_3:

                    # append to mult_both list
                    mult_both.append(element)

                    # remove element from mult_3 and mult_5
                    mult_3.remove(element)
                    mult_5.remove(element)

    # create a master list of all the multiples by appending
    total_list = []
    total_list.extend(mult_3)
    total_list.extend(mult_5)
    total_list.extend(mult_both)

    # return the total list of all multiples
    return total_list

########################################################################################################################

def main():

    # explain to user the purpose of the program
    print("This program calculates the sum of the multiples of 3 and 5 below a chosen number.")
    print("Enter 'done' to exit the program.\n")

    # use a while loop to keep the program running until the user wants to quit

    keep_going = True

    while keep_going:

        # ask user for a ceiling number
        num = int(input("Please enter a positive integer as a ceiling: "))
        print()

        # user wants to exit program
        if num == 'done':
            keep_going = False

        # user wants to continue with program
        else:
            # call mupltiples function
            mult_list = sorted(multiples(num))

            # add together all the elements of the list of multiples

            # initialize a total
            total = 0

            # print the multiples and their sum
            print("All of the multiples of 3 and 5 under" , num , "are:")

            # use a for loop to traverse the list
            for i in mult_list:

                # print the number with a space at the end
                print(i , end=' ')

                # use an accumulator to add each multiple to the total
                total += i

            # print the total
            print("\n\nThe sum of all the multiples of 3 and 5 under " , num , " is " , total , "." , sep='')
            print("\nThere are also " , len(mult_list) , " multiples of 3 and 5 under " , num , "." , sep='')
            print("\n\n\n")



########################################################################################################################

main()
