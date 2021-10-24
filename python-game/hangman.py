import random

HANGMANPICS = ['''

    +---+
    |   |
        |
        |
        |
        |
============''','''

    +---+
    |   |
    O   |
        |
        |
        |
============''','''

    +---+
    |   |
    O   |
    |   |
        |
        |
============''','''

    +---+
    |   |
    O   |
   /|   |
        |
        |
============''','''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
============''','''

    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
============''','''

    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
============''']
words = 'ant badger bat bear camel cat crow deer dog duck eagle \
        fox goat hawk lion llama monkey moose mouse otter owl panda \
        python rabbit rat raven salmon seal shark sheep skunk sloth \
        snake swan tiger turkey turtle whale wolf zebra'.split()

def getRandomWord(wordList):
    # this function returns a random string from the passed list of string.
    WordIndex = random.randint(0, len(wordList) - 1)
    return wordList[WordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # return the letter the player entered. This function makes sure the player entered a single letter, and not something else
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in alreadyGuessed:
            print("You have already guessed that letter. Choose again.")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Please enter a Letter")
        else:
            return guess

def playAgain():
    # this function return True if the player wants to play again, otherwise return False.
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith('y')


print("H A N G M A N")
missedLetters = ""
correctLetters = ""
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)

    # Let the player type in a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! the secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
        else:
            missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost
        if len(missedLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print("You have run out of guesses and " + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

        # ask the player if they want to play again (but only if the game is done).
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break


