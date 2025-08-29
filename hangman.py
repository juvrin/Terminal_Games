from random import randint
import re

with open('sowpods.txt', 'r') as f:
  lines_raw = f.readlines()

lines = [line.strip() for line in lines_raw]
word = lines[randint(0,len(lines))].lower()

blanks = '_' * len(word)
output = list(blanks)
letters = []
print("Welcome to Hangman!")

feedback = ''
count = 0

while count < 6:
    if feedback != word:
        letter = input("Guess your letter (type 'exit' to quit): ").lower()
        indices = [m.start() for m in re.finditer(letter, word)]
        if letter == 'exit':
            break
        if letter in letters:
            print("You've already guessed this letter!")
        elif len(indices) == 0:
            print("Incorrect!")
            letters.append(letter)
            count += 1
            guesses_left = 6 - count
            print(f"You have {guesses_left} guesses left.")
        elif len(indices) != 0:
            for i in indices:
                output[i] = letter
            print(' '.join(output))
            feedback = "".join(output)
            letters.append(letter)
            count += 1
            guesses_left = 6 - count
            print(f"You have {guesses_left} guesses left.")
    else:
        print(f"Congratulations! You have guessed the word in {count} guesses.")
        break

if feedback != word:
    print(f"Too bad! The word was {word}.")
