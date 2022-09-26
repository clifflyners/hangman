#import a python module
import random
#Create a list of your favorite fruits
word_list = ["apple", "banana", "pineapple", "mango", "grapes"]
# print(word_list)
#Using the random module, randomly print one of your favorite fruit
word = random.choice(word_list)
print(word)
#Using the input function, ask the user to input a letter

# Ensure the input is one letter

def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")
        lower_guess = guess.lower()
        def check_guess(lower_guess):
                    if len(lower_guess) == 1 and lower_guess.isalpha():
                        if lower_guess in word:
                            print("Good job!!!!", lower_guess, "is correct")
                        
                        else:
                            if lower_guess not in word:
                                print("Too Bad!!!!", lower_guess, "is not correct")
                                
                   
                    else:
                        print("Oops! that is not a valid input")
                        
        check_guess(lower_guess)
        break
ask_for_input()
      

            
                    