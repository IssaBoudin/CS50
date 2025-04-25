# Monty Py-Thon: The Math Game

A small, terminal-based Python game that challenges the player to solve ten math equations in 60 seconds. It shows ASCII art (using cowsay), big banners (using PyFiglet), emits nostalgics sounds (using pygame & simpleaudio) and colorful text (using Colorama) to add dimension. Perfect for practicing mental math!

---

# Video Demo
```https://youtu.be/5axew1DRxIU```
## Table of Contents

1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Prerequisites & Dependencies](#prerequisites--dependencies)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Code Walkthrough](#code-walkthrough)  
    - [main()](#main)  
    - [countdown()](#countdown)  
    - [get_level()](#get_level) 
    - [addition()](#addition)
    - [subtraction()](#subtraction)
    - [multiplication()](#multiplication)
    - [division()](#division)
    - [generate_integer()](#generate_integer)  
    - [figlet()](#figlet)  
7. [Extending or Customizing](#extending-or-customizing)  
8. [Troubleshooting](#troubleshooting)  
9. [Contributing](#contributing)  
10. [License](#license)

---

## Project Overview

This game measures how many addition sums you can correctly answer under a one-minute countdown. Players choose between three difficulty levels:
- **Level 1:** Single-digit sums (0–9)  
- **Level 2:** Double-digit sums (10–99)  
- **Level 3:** Triple-digit sums (100–999)  

Each problem allows up to three attempts; failed attempts reveal the correct answer. When time is up—or once ten questions have been asked—the game ends with a big Figlet banner displaying your final score.

---

## Features

- **Multithreaded countdown timer:** Runs in parallel so that the quiz loop stops when time’s up.  
- **Retry logic:** Three tries per question, with instant feedback (“EEE” on wrong input).  
- **ASCII graphics:**  
  - **cowsay**: Presents each problem inside a cartoon cow speech bubble.  
  - **PyFiglet**: Renders the final score as large, slanted ASCII art.
  - **pygame & simpleaudio**: Plays fun arcade music  
- **Colorful terminal output:** Uses ANSI escape codes via Colorama for red timer text, bold accents, and yellow banners.

---

## Prerequisites & Dependencies

- **Python 3.6+** (tested on 3.8, 3.9)  
- Third-party modules (install via `pip`):
  - `cowsay`  
  - `pyfiglet`  
  - `colorama`
  - `pygame`
  - `simpleaudio`  

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/IssaBoudin/project.git
   cd project

## Usage

```bash
python project.py
```

## Code Walkthrough
Functions:

`pick()`: **Asks the user if they want addition, subtraction, multiplication, or division.**

`countdown()`: **Starts a sleep timer to provide a simulated gameplay "feel." It's capable of applying Figlet to the final score should the user run out of time.**

`get_level()`: **Prompts the user for which level of difficulty they'd like to play, and passes that value to ```generate_integer()```.**

`addition()`: **Calls on generate_integer() to generate 10 randomized addition equations.**

`subtraction()`: **Calls on generate_integer() to generate 10 randomized subtraction equations.**

`multiplication()`: **Calls on generate_integer() to generate 10 randomized multiplication equations.**

`division()`: **Calls on generate_integer() to generate 10 randomized division equations.**

`generate_integer()`: **Takes value given from ```get_level()``` and uses the appropriate randint module to randomize integers; respectively, x & y values. These get stored inside the equation "```x + y =```", and the user is prompted to provide the answer.**

`figlet()`:  **Takes the score value given from the appropriate function, converts it back to a string, and passes it to figlet for processing. Figlet will generate a banner displaying the user's score once all equations are answered, or if the countdown timer hits zero.**

## Extending or Customizing

The user can further customize this script to include sound files of their choice; or, remove them entirely.

## Troubleshooting

**Install correct version of required dependencies.**
- Check the version of your dependencies by executing the following in your terminal:

      pip show colorama
      pip show pyfiglet
      pip show cowsay
      pip show pygame
      pip show simpleaudio
- Download the dependencies from **requirements.txt** if applicable.

      pip install -r requirements.txt
      pip3 install -r requirements.txt
- Or use pip

      pip install colorama, pyfiglet, cowsay, pygame, simpleaudio

## Contributing

**Word from IssaBoudin**
    - PLEASE feel free to find unique ways to grow this program!

## License
I believe the MIT license would be appropriate to add here; but, I'm not sure. Use this code. Seriously, I don't care.
