# This program allows a user to encode and decode messages through the use of a shift cipher.

# June 12th, 2018

def encrypt(key , message , alphabet):
    # this function takes a "message" as a string and encrypts it by shifting the characters of the string forward by an integer key

    # keep only a-z characters of the message and initialize the reduced message
    red_message = ''
    for char in message:
        if char.lower() in alphabet:
            red_message += char

    # initialize the final, encrypted string
    result_string = ''

    # traverse the string, shifting the characters by the key, and appending to the result string
    for char in red_message:
        ind = alphabet.index(char.lower())
        new_ind = (ind + key) % 26 # mod 26 because of the alphabet
        result_string += alphabet[new_ind]

    print("Your encrypted message is:")
    print(result_string.upper())

    return(result_string)

def decrypt(key , message , alphabet):
    # this function takes an encrypted, string message and decrypts it using an integer key

    # format the message
    message.lower()

    result_string = ''
    for char in message.lower():
        ind = alphabet.index(char)
        new_ind = (ind - key) % 26
        result_string += alphabet[new_ind]

    print('Your decrypted message is:')
    print(result_string)

    return(result_string)

def main():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    process = input('Would you like to encrypt ("e") or decrypt ("d") (enter "done" to exit)?\t')

    while process != 'done':

        if process == 'e':

            message = input("What would you like to encrypt?\t")

            key = int(input("How many places would you like to shift the characters by?\t"))

            print()
            enc = encrypt(key , message , alphabet)
        else:

            message = input("What would you like to decrypt (only letters)?\t")

            key = int(input("How many places would you like to shift the characters by?\t"))

            print()
            dec = decrypt(key , message , alphabet)

        print("\n\n\n")
        process = input('Would you like to continue to encrypt ("e") or decrypt ("d") (enter "done" to exit)?')


main()