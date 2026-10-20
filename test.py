import random


def random_message():
	messages = [
		"Keep exploring!",
		"A surprising result appeared.",
		"Randomness is useful for testing.",
	]
	return random.choice(messages)


if __name__ == "__main__":
	print(random_message())
