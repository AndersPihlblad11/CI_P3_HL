from random import *
import os
from art import logo, vs
from game_data import data


#______________________________________
def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

#______________________________________

def main_higher_lower(score = 0, first = choice(data), second = choice(data)):
	first_a = first
	second_a = second
	total_score = score

	clear_screen()
	print(logo)

	if total_score > 0:
		print(f"You're right! Current score: {total_score}")
		first_a = second_a
	second_a = choice(data)

	print(f"Compare A: {first_a['name']},  {first_a['description']}, from {first_a['country']}.\n{vs}")
	print(f"Against B: {second_a['name']},  {second_a['description']}, from {second_a['country']}")

	guess = input("Who is Faster? Type 'A' or 'B': ")
	more_speed = compare(first_a, second_a)

	if guess == 'A' and more_speed == "first" or guess == 'B' and more_speed == "second":
		total_score += 1
		main_higher_lower(total_score, first_a, second_a)
	else:
		print("You're Loose!")

		if input("Repeat? 'y' or 'n': ")== 'y':
			main_higher_lower(0, choice(data), choice(data) )
		else:
			print("Good bye!")


#______________________________________

def compare(first, second):
	if first['speed_count'] > second['speed_count']:
		return "first"
	else:
		return "second"

#_______________________________________

main_higher_lower()