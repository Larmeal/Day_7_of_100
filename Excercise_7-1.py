# Hangman game Step 1 ตรวจสอบว่า ตัวอักษรที่พิมพ์เข้ามาตรงกับคำศัพท์ที่สุ่มไหม

# My version
import random
def split(choose_word):
    return list(choose_word)

word_list = ["aardvark", "baboon", "camel"]

choose_word = random.choice(word_list)
number_word = len(choose_word)
word_split = split(choose_word)

input_guess = input("Guess a letter: ").lower()
guess = input_guess

for a in range(0, number_word):
    if guess == word_split[a]:
        print("Correct")
    else:
        print("Wrong")

# My teacher version


# import random

# word_list = ["aardvark", "baboon", "camel"]

# choose_word = random.choice(word_list)

# guess = input("Guess a letter: ").lower()

# for letter in choose_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")