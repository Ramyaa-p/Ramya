import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'strawberry', 'blueberry', 'kiwi']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nAttempts left:", attempts)
        print("Word:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            if set(word) == set(guessed_letters):
                print("Congratulations! You've guessed the word:", word)
                break
        else:
            print("Incorrect guess.")
            attempts -= 1

    else:
        print("Sorry, you ran out of attempts. The word was:", word)


hangman()
