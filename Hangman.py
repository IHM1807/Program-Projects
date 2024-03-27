# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random

def choose_word():
    words = ['python', 'hangman', 'programming', 'computer', 'game', 'player', 'code']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("Try to guess the word before the hangman is completed.")

    while attempts_left > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts_left)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
            if display_word(word, guessed_letters) == word:
                print("\nCongratulations! You've guessed the word:", word)
                break
        else:
            print("Incorrect guess.")
            attempts_left -= 1

    if attempts_left == 0:
        print("\nSorry, you've run out of attempts. The word was:", word)

hangman()