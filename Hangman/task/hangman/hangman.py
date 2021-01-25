import random

words = ['python', 'java', 'kotlin', 'javascript']
upper_letters = 'QWERTYUIOPASDFGHJKLZXCVBNM'
answer = (random.choice(words))
hidden = list("-" * len(answer))
guesses = []
attempts = 8

print("H A N G M A N")

menu = input('Type "play" to play the game, "exit" to quit:')

while True:
    print()
    print(''.join(hidden))
    print('Input a letter: ', end="")
    letter = input()

    if len(letter) != 1:
        print("You should input a single letter")
    elif letter in upper_letters or not letter.isalpha():
        print("Please enter a lowercase English letter")
    elif letter in guesses or letter in hidden:
        print("You've already guessed this letter")
        guesses.append(letter)
    elif letter not in answer:
        print("That letter doesn't appear in the word")
        attempts -= 1
        guesses.append(letter)

    else:
        for x in range(len(answer)):
            if letter == answer[x]:
                hidden[x] = letter
            x += 1

    if hidden == list(answer):
        print("You guessed the word!")
        print("You survived!")
        break
    if attempts == 0:
        print("You lost!")
        break
