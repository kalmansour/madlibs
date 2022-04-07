def main():
	print("Mad libs where libs get mad.")
	print("Start below:\n")

	time = input('Enter a number from 1 to 12:')
	items = input('Enter a noun (plural):')
	name = input('Enter a name:').title()
	scream = input('Enter any sentence:').upper()
	action = input('Enter a verb:')
	story = f"It was {time} o'clock when I heard a knock at the door."f"\nI opened the door and there was a box full of {items} with a note saying \"From {name}\"."f"\nJust as I closed the door I heard a scream \"{scream}.\""f"\nI froze in place and all I could do was {action}."

	print("\nThe story goes...\n")

	print(story)

if __name__ == '__main__':
	main()