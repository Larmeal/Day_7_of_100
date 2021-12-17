#Step 3 ถามวน loop ไปเรื่อย ๆ จนกว่าจะเติมอักษรได้จนครบ

# My version

def split(split_word):
    return list(split_word)
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
split_word = split(chosen_word)

print(f'Pssst, the solution is {chosen_word}.')

display = []
for length in range(word_length):
    display += "_"

while display != split_word:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    print(display)
print("You win")



# My teacher version
# import random
# word_list = ["aardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
# split_word = split(chosen_word)

# print(f'Pssst, the solution is {chosen_word}.')

# display = []
# for _ in range(word_length):
#     display += "_"

# finish_game = False

# while display != finish_game:
#     guess = input("Guess a letter: ").lower()

#     for position in range(word_length):
#         letter = chosen_word[position]
#         print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     print(display)
#     if "_" not in display:
#         finish_game = True
#         print("You win")
