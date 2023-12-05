# Strong Password Generator

import string
import random


s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

numChars = input('How many characters do you need for the password? : ')

while True:
    try:
        numChars = int(numChars)
        if numChars < 6 :
            print('You need at least 6 characters')
            numChars = input('Please enter the number again: ')
        else:
            break
    except:
        print('Please enter numbers only')
        numChars = input('How many characters do you need for the password? : ')
        
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

p1 = round(numChars * (30/100))
p2 = round(numChars * (20/100))

password = []

for i in range(p1):
    password.append(s1[i])
    password.append(s2[i])


for i in range(p2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)

password = "".join(password[0:])
print(password)