import random
from tkinter import Tk, Canvas

root = Tk()
root.title("Hangman")
canvas = Canvas(root, width=400, height=400)
canvas.pack()


def draw_hangman(attempts):
    if attempts == 6:
        # Draw the base
        canvas.create_line(50, 350, 350, 350, width=5)
        canvas.create_line(200, 50, 200, 350, width=5)
        canvas.create_line(100, 350, 200, 50, width=5)
        canvas.create_line(200, 50, 300, 350, width=5)
    elif attempts == 5:
        # Draw the head
        canvas.create_oval(150, 100, 250, 200, width=5)
    elif attempts == 4:
        # Draw the body
        canvas.create_line(200, 200, 200, 300, width=5)
    elif attempts == 3:
        # Draw the left arm
        canvas.create_line(200, 220, 150, 250, width=5)
    elif attempts == 2:
        # Draw the right arm
        canvas.create_line(200, 220, 250, 250, width=5)
    elif attempts == 1:
        # Draw the left leg
        canvas.create_line(200, 300, 150, 350, width=5)
    else:
        # Draw the right leg
        canvas.create_line(200, 300, 250, 350, width=5)

def select_word():
    word_list = ["python", "java", "ruby", "javascript", "html", "css"]
    return random.choice(word_list)

def display_word(word, guesses):
    displayed_word = ""
    for letter in word:
        if letter in guesses:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def process_guess(word, guesses, guess):
    if guess in guesses:
        return "You've already guessed that letter!"
    guesses.append(guess)
    if guess in word:
        return "Good guess!"
    else:
        return "Wrong guess!"

def play_hangman():
        word = select_word()
        guesses = []
        attempts = 6

        print("Let's play Hangman!")

        while attempts > 0:
            print("Attempts remaining:", attempts)
            print(display_word(word, guesses))

            guess = input("Enter your guess: ")

            result = process_guess(word, guesses, guess)
            print(result)

            draw_hangman(6-attempts)

            if "_" not in display_word(word, guesses):
                print("Congratulations! You won!")
                break

            if result == "Wrong guess!":
                attempts -= 1

        if attempts == 0:
            print("Sorry, you lost. The word was:", word)

        root.mainloop()


play_hangman()