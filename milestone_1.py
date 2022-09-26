#import a python module
import random
#Create a list of your favorite fruits
word_list = ["apple", "banana", "pineapple", "mango", "grapes"]
# print(word_list)
#Using the random module, randomly print one of your favorite fruit
word = random.choice(word_list)
print(word)
#Using the input function, ask the user to input a letter
guess = input("Enter a single letter: ")
# Ensure the input is one letter
if len(guess) == 1 and guess.isalpha():
        print("Good guess")
else:
        print("Oops! that is not a valid input")
            



