#Step 5 ขั้นตอนสุดท้าย

import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
Hold = "_"

print(hangman_art.logo)
# สูตรโกง
# print(f'Pssst, the solution is {chosen_word}.')

# กำหนด scope ของคำที่สุ่มมา
display = []
for _ in range(word_length):
    display += "_"

# ขั้นตอนการ input ตัวอักษรที่เดาว่าตรงกับคำที่สุ่มมาไหม
while not end_of_game:
    # แจ้งเตือนการใส่ตัวอักษรเดิม
    guess = input("Guess a letter: ").lower()
    if guess in display:
            print(f"You've already guessed {guess}")
    # ตรวจสอบว่า ตักอักษรตรงกับตำแหน่งบ้างในคำที่สุ่มมา
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # กรณีเลือกตัวอักษรมาผิด ก็จะโดนหักคะแนน
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a lift.")
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # ถ้าใส่ตัวอักษรมาครับก็จะชนะ
    if Hold not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])