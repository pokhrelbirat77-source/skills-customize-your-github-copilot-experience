
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman game in Python to practice string handling, loops, conditionals, and user input.

## 📝 Tasks

### 🛠️ Create the Game Loop

#### Description

Write the main game loop that selects a random word and lets the player guess letters until they win or run out of attempts.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list
- Display the word progress with underscores for hidden letters
- Allow the player to guess one letter at a time
- Update the display after each guess
- End the loop when the word is fully guessed or the player has no attempts left

### 🛠️ Handle Guesses and Game State

#### Description

Implement guess validation, incorrect guess tracking, and messages for win or loss.

#### Requirements
Completed program should:

- Reject repeated guesses and prompt the player again
- Track and display the number of incorrect guesses remaining
- Show a win message when the player guesses the full word
- Show a loss message when the player runs out of attempts
- Reveal the correct word after the game ends

### 🛠️ Add User Feedback

#### Description

Improve the game experience with clear prompts and progress updates.

#### Requirements
Completed program should:

- Prompt the player to enter a letter for each guess
- Show the current word progress after each guess
- Display letters guessed so far or the number of remaining attempts
- Use clear text output for game status updates
