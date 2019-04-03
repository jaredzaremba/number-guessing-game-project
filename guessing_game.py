"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
import os


High_Scores = []
def start_game():
        
    
    
    print(""" 
    Welcome to The Number Guessing Game!
    The rules are simple, you have to guess a number between 1 and 20.
    If you guess wrong that's ok. I'll be there to help you out! 
    Try to get the correct number in the least amount of tries. Good Luck!""")
    

    
    
    
    
    min_number = 1
    max_number = 20
    answer = random.randint(min_number, max_number)
    guesses = 0
    Game_state = True
    
    while Game_state == True:
        
        try:
            Guess = int(input("Guess a number between 1 and 20:  "))
        except ValueError:
            print("Sorry that's not a number try again!")
            continue
        try:    
            if Guess < min_number or Guess > max_number:
                raise ValueError
        except ValueError as err:
                print("That number isn't in the range, try again!")
                continue
            
        if Guess == answer:
            guesses += 1
            High_Scores.append(guesses)
            break
            
        elif Guess < answer:
            guesses += 1
            print("It's higher  ")
            continue
            
        else:
            guesses += 1
            print("It's lower  ")
            continue
            
            

            
    print("""
    Congrats you got it! It took you {} guesses! 
    The game is ending.  """.format(guesses))
    
    again = input("Would you like to play again? Enter (Y/N):  ")
    if again[0].lower() == "y":
        High_Scores.sort()
        for score in High_Scores:
            High_Scores[::-1]
        print("""
    See if you can beat the best!
    High Scores: {}  """.format(High_Scores))
        start_game()
    else:
        print("Ok thanks for playing!")
        
    
    
        
        
    
    
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

   
