import random 

with open("words.txt") as file:
    words = file.readlines()

# create a list of random words from text file
random_list = random.sample(words,3)
print(random_list)

# pick a random word from list 
random_word = random.choice(random_list).strip().lower()
print(random_word)

# Now we have to generate as many blanks as letters in word
str = ""
for blank in range (len(random_word)):
    str = str +'_'
print(str)

# Ask the user to guess a letter
guess = input("Guess a letter: ").lower()

# Now check whether the letter guess by the user is present in the word 
word = ""
for i in range (len(random_word)):
    if random_word[i] == guess:
        str = str.replace(str(i),guess)
else:
    print("Guessed the wrong letter")
 
print(str)
