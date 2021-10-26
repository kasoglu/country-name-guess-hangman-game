import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

print(logo)
print("Game Rules:\n")
print("1- This game about Country Names.\n")
print("2- You can just enter same value one time.\n")
print("3- If you enter empty value you will lose a life.\n")


game_is_finished = False
lives = len(stages) - 1

#Game choose random country names from Word List
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Create blanks for word
display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    #clear() function imported from replit to clear the output between guesses.
    clear()

    #If user guessed same letter already before program will execute this line.
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter true or false. 
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    #Checking if user entered a wrong value.
    if guess not in chosen_word:
        print(f"You guessed '{guess.upper()}' and that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print("You lose.")

    #Checking if user entered a empty value.
    if guess == '':
      print("\nYou can not enter empty value.")
    
    # If user guessed all letters true finish game.
    if not "_" in display:
        game_is_finished = True
        print("Congrutulations, You won.")
    
    #Execute the hangman lives by visual.
    print(stages[lives])