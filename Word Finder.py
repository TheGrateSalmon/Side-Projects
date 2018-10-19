def main():
    text = input("Enter a string or 'done' to quit: ")

    while text != "done":
        print()

        text_list = text.split()

        index = int(input("Which word place? ")) - 1

        print("The word is:", text_list[index])

        print()

        text = input("Enter a string or 'done' to quit: ")


main()