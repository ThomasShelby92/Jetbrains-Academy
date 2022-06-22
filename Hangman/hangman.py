# Write your code here
import random

w_score = 0
l_score = 0

def play():
    global w_score, l_score

    l = ['python', 'java', 'swift', 'javascript']
    correct_word = random.choice(l)
    guessing_word = ""
    letter = ""
    attempts = 8
    for x in range(0, len(correct_word)):
        guessing_word = guessing_word + "-"
    guessing_word = list(guessing_word)
    guesses = set()

    while True:
        print("".join(guessing_word))
        print(f"Input a letter:")
        letter = input()
        if len(letter) != 1:
            print("Please, input a single letter.")
            continue
        elif letter.islower() == 0:
            print("Please, enter a lowercase letter from the English alphabet.")
            continue
        print(f" # {attempts} attempts")
        if letter in guesses:
            print("You've already guessed this letter.")
            continue
        else:
            guesses.add(letter)
        if letter in correct_word and letter not in guessing_word:
            for j in range(0,len(correct_word)):
                if letter == correct_word[j]:
                    guessing_word[j] = letter
        elif letter in guessing_word:
            print("You've already guessed this letter.")
        else:
            print("That letter doesn't appear in the word.")
            attempts -= 1
        if "".join(guessing_word) == correct_word:
            print("".join(guessing_word))
            print(f"You guessed the word {correct_word}!")
            print("You survived!")
            w_score += 1
            break
        if attempts == 0:
            print("You lost!")
            l_score += 1
            break

def score():
    print(f"You won: {w_score} times")
    print(f"You lost: {l_score} times")



print(f"H A N G M A N  # 8 attempts")
print("")


while True:
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    menu = input()
    if menu == "play":
        play()
        continue
    elif menu == "results":
        score()
        continue
    elif menu == "exit":
        break




print("Thanks for playing!")
#
# if word == correct_word:
#     print("You survived!")
# else:
#     print("You lost!")
