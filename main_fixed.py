# Display art
# Generate random account
# format account data
# ask user to guess
# check if user is correct
## get follower 
## use if statement to check if user is correct
# give user feedback on their guess
# make game repeatable
# swap b to a and generate new random b

from art import logo, vs
import game_data import data
import random
import os

# Function to clear the screen
def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def format_data(account):
  """Format the account data into printable format"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_follower_count, b_follower_count):
  """Take the user guess and follower counts and returns if they got it right"""
  if a_follower_count > b_follower_count:
    return guess == "a"
  else:
    return guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data) # reason to put outside, so this wont be used when the game continue, it stuck in the while loop until the game end

while game_should_continue:
  account_a = account_b
  account_b = random.choice(data)

  if account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Compare B: {format_data(account_b)}")

  # ask user for a guess
  guess = input("Who has more followers? Type 'a' or 'b': ").lower()

  # check follower number
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  clear_screen()

  if is_correct:
    score += 1
    print(f"You are right! Current score: {score}")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final Score: {score}")
