import random
from art import logo, vs
from game_data import data
import os

# Function to clear the screen
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

# pick someone randomly
# Write a conditino that the 2 pick != to each other

def randomPeople (data):
  random_person1 = random.choice(data)
  random_person2 = random.choice(data)
  return random_person1, random_person2

"""
If you want to use the randomly chosen people outside of the function, you need to return them from the function. This is why we include random_person1 and random_person2 as return values. This allows you to capture the results of the function call and use them elsewhere in your code, like printing them or doing some other operations.
"""

# Greet Screen and user input
def userInput():
  clear_screen() # clear the screen before each new round
  print(logo)
  print(f"Compare A: {random_person1['name']},{random_person1['description']},{random_person1['country']}")
  print(vs)
  print(f"Compare B: {random_person2['name']},{random_person2['description']},{random_person2['country']}")
  return input("Who has more followers? Type 'A' or 'B': ").lower()


# Now, we compare them 
end_of_game = False
win_counter = 0

def compareThem(random_person1, random_person2):
  global win_counter
  global end_of_game
  
  while not end_of_game:
    InputData = userInput()

    print(f"\n\nTop follower number {random_person1['follower_count']}")
    print(f"Top follower number {random_person2['follower_count']}\n\n")
    # Check follower counts and swap if necessary
    if random_person2["follower_count"] > random_person1["follower_count"]:
      temp = random_person1
      random_person1 = random_person2
      random_person2 = temp
      correct_answer = "b"
    else:
      correct_answer = "a"
    

    if InputData == correct_answer:
      print("You're right!")
      win_counter += 1
      random_person1 = random_person2
      random_person2 = random.choice(data) # Swap place and only generate one random to continue
      while random_person2 == random_person1: # make sure 2 random won't match
        random_person2 = random.choice(data)
    else:
      print(f"You're wrong. Game Over and your score: {win_counter}")
      end_of_game = True

    random_person1, random_person2 = randomPeople(data)

#start the game
random_person1, random_person2 = randomPeople(data)
compareThem(random_person1, random_person2)

"""
I noticed there is an issue when the answer match the user input, the screen will not refresh and pick a new question. 
"""