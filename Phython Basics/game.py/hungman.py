import random
import hungman_stage
word_list = ["apple", "beautiful","potato"]
choosen_word = random.choice(word_list)
print(choosen_word)
display = []
for i in range(len(choosen_word)):
    display += '_'
print(display)
game_over = False
lives = 0
while not game_over:
    guess = input("Guess a letter: ")
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess:
            display[position] = guess
    print(display)

    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print('You Loose')
    if '_' not in display:
        print('You win')
    print(hungman_stage.stages[lives])