import random
import cowsay
from pyfiglet import Figlet
import time
import threading
import os
from colorama import Fore, Back, Style
#Keep welcome message from popping up.
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import simpleaudio as sa

#If not using git to clone the repo, do the following:
#Ensure the audio .wav files are present in the same directory as the program!
#wget https://github.com/IssaBoudin/CS50/blob/main/music/CorrectSound.wav
#wget https://github.com/IssaBoudin/CS50/blob/main/music/NegativeGuitar.wav
#wget https://github.com/IssaBoudin/CS50/blob/main/music/WorldMusic.wav


RED = "\033[31m"
RESET = "\033[0m"
YELLOW = "\033[1;33m"
BOLD = "\033[1m"

score = 0
pygame.mixer.init()
try:
    pygame.mixer.music.load("WorldMusic.wav")
    pygame.mixer.music.play(loops=-1)
except pygame.error as e:
    print(f"Error playing music: {e}")

def main():
    pick()

def pick():
    while True:
        choice = input("Choose: [1] Addition [2] Subtraction [3] Multiplication [4] Division: ")
        if choice == "1":
            addition()
        elif choice == "2":
            subtraction()
        elif choice == "3":
            multiplication()
        elif choice == "4":
            division()

def countdown():
    time.sleep(60)
    print(f"\n\n{RED}{BOLD}⏰ GAME OVER!⏰{RESET}")
    pygame.mixer.music.stop()
    sa.WaveObject.from_wave_file("NegativeGuitar.wav").play().wait_done()
    time.sleep(2)
    figlet(f"Score: {score} / 10")

def get_level():
    while True:
        try:
            level = int(input("Level (1/2/3): "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass

def addition():
    global score
    level = get_level()
    timer = threading.Thread(target=countdown, daemon=True)
    timer.start()
    print(f"{RED}COUNTDOWN: 60 SECONDS{RESET}")
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for _ in range(3):
            cowsay.cow(f"{x} + {y} = ")
            try:
                answer = int(input("\nYour Answer: "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} + {y} = {x + y}")

    figlet(f"Score: {score} / 10")

def subtraction():
    global score
    level = get_level()
    timer = threading.Thread(target=countdown, daemon=True)
    timer.start()
    print(f"{RED}COUNTDOWN: 60 SECONDS{RESET}")
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        while x < y:
            x = generate_integer(level)
            y = generate_integer(level)

        for _ in range(3):
            cowsay.cow(f"{x} - {y} = ")
            try:
                answer = int(input("\nYour Answer: "))
                if answer == x - y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} - {y} = {x - y}")

    figlet(f"Score: {score} / 10")

def multiplication():
    global score
    level = get_level()
    timer = threading.Thread(target=countdown, daemon=True)
    timer.start()
    print(f"{RED}COUNTDOWN: 60 SECONDS{RESET}")
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for _ in range(3):
            cowsay.cow(f"{x} x {y} = ")
            try:
                answer = int(input("\nYour Answer: "))
                if answer == x * y:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} x {y} = {x * y}")

    figlet(f"Score: {score} / 10")

def division():
    global score
    level = get_level()
    timer = threading.Thread(target=countdown, daemon=True)
    timer.start()
    print(f"{RED}COUNTDOWN: 60 SECONDS{RESET}")
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        while y == 0 or x % y != 0:
            x = generate_integer(level)
            y = generate_integer(level)
        result = x // y

        for _ in range(3):
            cowsay.cow(f"{x} / {y} = ")
            try:
                answer = int(input("\nYour Answer: "))
                if answer == result:
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
        else:
            print(f"{x} / {y} = {result}")

    figlet(f"Score: {score} / 10")

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)
    
def figlet(final):
    f = Figlet()
    f.setFont(font="slant")
    converted = f.renderText(final)
    print(f"{YELLOW}{converted}{RESET}")
    sa.WaveObject.from_wave_file("CorrectSound.wav").play().wait_done()
    os._exit(0)

if __name__ == "__main__":
    main()
