"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.  - - - > DONE
    2. Store a random number as the answer/solution.    - - - > DONE
    3. Continuously prompt the player for a guess.
      a. If the guess is greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
print("--" * 18)
print(" Welcome to the Number Guesing Game!")
print("--" * 18)
print()


random_number = random.randint(1, 10)
count = 1


while True:
  while True:

    try:
      guess = int(input("Pick a number between 1 and 10. --> "))

    except ValueError:
      print("Oops, you need to enter a number.")
      count += 1
      continue
    
    if guess < 1 or guess > 10:
      print("Oops. The number has to be between 1 and 10.")
      continue
      
    elif guess > random_number:
      print("\nIt's lower.\n")
      count += 1
      continue
      
    elif guess < random_number:
      print("\nIt's higher.\n")
      count += 1
      continue

    elif guess == random_number:
      print()
      print("Nicely done!\n")
      break
      
    print("Congratulations! It took you {} tries\n".format(count))
  
  play_again = input("Would you like to play again? \nPlease, enter Yes or No. --> ")

  if play_again.lower() == "yes":
    print("All right! Here we go.")
    start_game()
  
  elif play_again.lower() == "no":
    print("Game over. I hope you had fun!")
    break

# Kick off the program by calling the start_game function.
start_game()