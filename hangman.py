import string
from colorama import Fore
import random as r
import os
import math
import json

class Hangman():
    def __init__(self):
        self.in_progress = None, True
        self.all_letters = list(string.ascii_lowercase)
        self.correct_letters, self.wrong_letters = [], []
        with open('words.json') as file: self.file = json.load(file)
        self.word = r.choice(list(self.file.keys()))
        self.guesses_remaining = math.ceil(len(self.word) * 1.25)

    def show_scoreboard(self):
        for letter in self.word:
            if letter in self.correct_letters:
                print(Fore.GREEN, letter, end = " ")
            elif letter in self.wrong_letters:
                print(Fore.RED, letter, end = " ")
            else:
                print(Fore.WHITE, "_", end = " ")
        print(Fore.WHITE, f"\n\nGuesses Remaining: {self.guesses_remaining}\n\n")
        
    def check_letter(self, letter):
        if letter in [x for x in self.word]:
            return True

    def guess_letter(self):
        print(Fore.WHITE, "Please choose a letter from the possible characters:\n")

        for letter in self.all_letters:
            if letter in self.wrong_letters:
                print(Fore.RED, letter, end = " ")
            elif letter in self.correct_letters:
                print(Fore.GREEN, letter, end = " ")
            else:
                print(Fore.WHITE, letter, end = " ")
        print(Fore.WHITE, "\n")
        letter = input("Please guess a letter: ")
        if self.check_letter(letter):
            self.correct_letters.append(letter)
        else:
            self.wrong_letters.append(letter)
        self.guesses_remaining -= 1
        os.system('cls' if os.name == 'nt' else 'clear')

    def check_win(self):
        if self.guesses_remaining == 0:
            self.in_progress = False
            print(Fore.WHITE, f"YOU FAILED!\n The correct word was: {self.word}")
        if set(self.correct_letters) == set([x for x in self.word]):
            self.in_progress = False
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.WHITE, f"You win!\nT he word was: {self.word}\n Guesses remaining: {self.guesses_remaining}")

        

    def start_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        while self.in_progress:
            self.show_scoreboard()
            self.guess_letter()
            self.check_win()