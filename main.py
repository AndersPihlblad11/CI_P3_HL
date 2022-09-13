from art import logo, vs
from game_data import data
import random

# Format the account data into printable format.
def format_data(account):
account_name = account_a ["name"]
account_name = account_a ["description"]
account_name = account_a ["country"]
return f"{account_name}, a {account_descr}, from {account_country}"
 
def check_answer(guess, a_followers, b_followers): 
    if a_followers > b_followers:
        return guess == "a"
        else:
            return guess == "b" 

# Higher Lower Display art
print(logo)
score = 0
# Generate a random account from the game data.
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_ = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(vs)
print(f"Compare B: {format_data(account_a)}.")

# Ask user for a guess.
input("Who has more followers? Type 'A' or 'B': ").lower()

# Check if user is correct.
# Get follower count of each account.
a_follower_count = account_a["follow_count"]
b_follower_count = account_b["follow_count"]

is_correct = check_answer(guess, a_follower_count, b_follower_count)
# Use if statement to check if user is correct.

# Give feedback on their guess.
if is_correct:
    score += 1
    print("Your right! Current score: {score}")
else:
    print("Sorry, thats wrong. Final score: {score}")

# Score keeping. 

# Making the game repeatable.

# Making account at position B become the next account at the position A.

# Clear the screen between rounds.