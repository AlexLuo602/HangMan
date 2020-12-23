import os
import time
import sys
clear = lambda: os.system('cls') #on Windows System
sentence = input("Choose your sentence or word: ").lower()
clear()
l = []
total_guesses = []
c = 0 #max chances is 6
game_over = 6
counter = 0
count = 6

hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def drawing():
    for i in range(0,7):
        if i == c:
            print (hangman_pics[i])

def main_section(x):
    if guess == sentence:
        clear()
        print("guesses: " + " ".join(total_guesses))
        drawing()
        print(sentence)
        time.sleep(2)
        print("You win!")
        sys.exit()
    for i in sentence:
        if guess == i and i not in l:
            l.append(guess)
            return x
            break
    if guess in total_guesses:
        print("You already guessed this number!")
        time.sleep(1)
        return x
    x = x + 1
    return x

def after():
    a = []
    for i in sentence:
        if i in l:
            a.append(i)
        elif i == " ":
            a.append(i + " ")
        else:
            a.append("_ ")
    print("".join(a))

def check_if_win():
    x = sentence.replace(" ", "")
    for i in l:
        if i in sentence:
            x = x.replace(i,"")
    if x == "":
        clear()
        print("guesses: " + " ".join(total_guesses))
        drawing()
        after()
        time.sleep(2)
        print ("You win!")
        sys.exit()

while c < game_over:
    print("guesses: " + " ".join(total_guesses))
    drawing()
    after()
    guess = input("Guess a character: ").lower()
    c = main_section(c)
    if guess not in total_guesses:
        total_guesses.append(guess)
    check_if_win()
    clear()
print (hangman_pics[6])
print ("the phrase was: " + sentence)
time.sleep(2)
print ("Game Over!")