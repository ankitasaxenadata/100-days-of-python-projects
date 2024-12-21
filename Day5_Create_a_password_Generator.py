import random

# Create a list with the alphabet from 'a' to 'z'
small_alphabet_list = [chr(i) for i in range(ord('a'), ord('z') + 1)]

# Create a list with the alphabet from 'A' to 'Z'
large_alphabet_list = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# create a list consist of upper case and lowercase alphabets
alphabet = small_alphabet_list + large_alphabet_list

# create a number list from 0 to 9
number_list = [str(i) for i in range(10)]

# create a list of symbols
symbols = ['!', '#', '$', '%', '&', '(',')', '*', '+']


User_letter = int(input("How many letters would you like in your password? \n"))
User_symbols = int(input("How many symbols would you like? \n"))
User_number = int(input("How many numbers would you like? \n"))
a = b = c = ''


for i in range(User_letter): # creating a loop for generating letters 
    a = a + random.choice(alphabet)
for j in range(User_symbols): # creating a loop for generating symbols
    a = a + random.choice(symbols)
for k in range(User_number): # creating a loop for generating number
    a = a + random.choice((number_list))

string = a # string after random selection
print(list(string))
shuffle = list ((''.join(random.sample(string,len(string))))) # shuffling the string to generate password for user so that it wont be a ordered password
print(shuffle)
print(''.join(shuffle))
   