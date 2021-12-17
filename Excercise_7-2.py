#Step 2 กำหนดขนาดของตัวอักษรของกลุ่มคำที่สุ่มมาได้ และแทนที่ตัวอักษรที่เดา

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

print(f'Pssst, the solution is {chosen_word}.')
length_word = len(chosen_word)

display = []
for length in range(0, length_word):
    display += "_"

guess = input("Guess a letter: ").lower()

for position in range(0, length_word):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = guess

print(display)