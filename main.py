from art import logo, vs
from game_data import data
import random

# Format the account data into printable format.
account_name = account_a["name"]
account_name = account_a["description"]
account_name = account_a["country"]
print(f"{account_name}, a {account_descr}, from {account_country}")

# Higher Lower Display art
print(logo)
# Generate a random account from the game data.
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_ = random.choice(data)

print(f"Compare A: {format_data(account_a)}.")
print(vs)
print(f"Compare B: {format_data(account_a)}.")

# Ask user for a guess.

# Check if user is correct.
# Get follower count of each account.
# Use if statement to check if user is correct.

# Give feedback on their guess.

# Score keeping. 

# Making the game repeatable.

# Making account at position B become the next account at the position A.

# Clear the screen between rounds.