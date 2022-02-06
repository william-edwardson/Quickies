# Simple strong password generator

import random

print('STRONG PASSWORD GENERATOR\n')

# charset for our passwords. Modify if necessary
#             lowercase letters         UPPERCASE LETTERS     numbers         symbols incl. space
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()_+-=`~[];\',./<>?:"{}\|'

while True:
    # user input (password parameters)
    numPasswords = int(input('How many passwords do you want to generate? (0 to exit) '))

    # 0 to exit
    if (numPasswords == 0):
        break
    
    numLetters = int(input('What is the target password length? '))

    print('\nYour {} passwords of length {}\n'.format(numPasswords, numLetters))

    for i in range(numPasswords):
        password = '' # initialise a blank password
        for j in range(numLetters):
            password += random.choice(chars) # get a random element from the charset
        print(password) # display the generated password
    print()
