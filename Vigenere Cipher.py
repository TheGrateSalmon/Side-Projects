# this program allows the user to encrypt and decrypt plaintext using a Vigenere (poly-alphabetic) cipher

# a Vigenere cipher takes a key, e.g. "cafe", and shifts each character in a block of characters by the corresponding value per character,
# i.e. "tellhimaboutme" (using the key "cafecafecafeca" [key length matches message length]) maps to "VEQPJIREDOZXOE"

# June 12th, 2018

########################################################################################################################

def plain_string(message , alphabet):
    # this function takes a string message and returns a new string of only valid letters (a-z)

    # initialize the new message
    new_string = ''

    # traverse the original message and keep only the a-z characters
    for char in message:

        if char in alphabet:
            new_string += char

    return new_string

########################################################################################################################

def vig_key(key , message , alphabet):
    # this function takes the key and creates the Vigenere key based on the length of the message by iterating over the message

    num_full = (len(message)) // (len(key))
    num_remain = (len(message)) % (len(key))

    # get the final part of the Vigenere key by taking part of the key through the remainder (only execute if remainder != 0)
    if num_remain != 0:
        part_new_key = key[:num_remain]
    else:
        part_new_key = ''

    # concatenate into full Vigenere key
    new_key = (key * num_full) + part_new_key
    new_key_lower = new_key.lower()

    # convert key into iterable list of integers corresponding to character (a -> 0 , b -> 1 , ...)
    key_int_list = []
    for char in new_key_lower:
        if char in alphabet:
            ind = alphabet.index(char)
            key_int_list.append(ind)

    return key_int_list

########################################################################################################################

def encrypt(key , message , alphabet):
    # this function encypts the string message using the list key

    # initialize index counter for Vigenere key
    key_counter = 0

    # create empty string to append to with the encrypted characters
    enc_message = ''

    for char in message:

        char_ind = alphabet.index(char)

        # add the original message character value and the key character value for new index for later use with alphabet index
        enc_ind = (char_ind + key[key_counter]) % 26

        # use new "encrypted index" to get new character from alphabet
        enc_char = alphabet[enc_ind]

        # add encrypted character to the total encrypted message
        enc_message += enc_char

        key_counter += 1

    # make encrypted message all upper case
    enc_message_upper = enc_message.upper()

    return enc_message_upper

########################################################################################################################

def decrypt(key , message , alphabet):
    # this function decrypts a string message using a list key

    # make the message all lower case
    lower_message = message.lower()

    # initialize the decrypted message string and key counter
    decrypted_message = ''
    key_counter = 0

    # traverse the message string
    for char in lower_message:

        # make sure each character in the string is in the a-z alphabet
        if char in alphabet:

            # convert to integer by using the associated index in alphabet list
            ind = alphabet.index(char)

            # subtract key from character value to obtain decrypted character value
            dec_ind = (ind - key[key_counter]) % 26

            # obtain a-z character by using index in alphabet list
            dec_char = alphabet[dec_ind]

            # add character to the decrypted message string
            decrypted_message += dec_char

            # add to key counter
            key_counter += 1

    return decrypted_message

########################################################################################################################

def main():

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    # ask the user if they want to encrypt of decrypt

    choice = input("Would you like to encrypt ('e') or decrypt ('d') (enter 'done' to exit)?\t")

    while choice != 'done':

        if choice == 'e':

            # ask user for message
            message = input("What would you like to encrypt?\t")
            lower_message = message.lower()

            # convert message to only a-z characters
            plain_message = plain_string(lower_message , alphabet)

            # ask user for key
            key = input("What key do you want to use?\t")

            # convert key to a usable Vigenere key
            new_key = vig_key(key , plain_message , alphabet)

            # encypt the message
            enc_message = encrypt(new_key , plain_message , alphabet)

            print()
            print("Your encrypted message is\n" , enc_message)

        elif choice == 'd':

            # ask user for message and key
            message = input("What would you like to decrypt?\t")
            lower_message = message.lower()

            # convert message to only a-z characters
            plain_message = plain_string(lower_message , alphabet)

            # ask user for key
            key = input("What key do you want to use?\t")

            # convert key to a usable Vigenere key
            new_key = vig_key(key , plain_message , alphabet)

            # decrypt the message
            dec_message = decrypt(new_key , plain_message , alphabet)

            print()
            print("Your decrypted message is\n" , dec_message)

        else:
            print("That is not a valid input. Please try again.")


        print('\n\n\n')
        choice = input("Would you like to encrypt ('e') or decrypt ('d') (enter 'done' to exit)?\t")

########################################################################################################################

main()