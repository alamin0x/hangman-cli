# Importing Requirement Recourses
import random
import Hangman_art
import Hangman_Word_list as HWL


# Defining Hints Function:
def hint(random_list):
    if random_list == HWL.list_of_animals:
        return "Its a name of Animal"
    elif random_list == HWL.list_of_colors:
        return "Its a name of Color"
    elif random_list == HWL.list_of_citys:
        return "Its a Name of City in Bangladesh"


# Displaying Logo
print(Hangman_art.logo)

# Making Random Word
list_of_words = [HWL.list_of_animals, HWL.list_of_colors, HWL.list_of_citys]
random_list = random.choice(list_of_words)
word = random.choice(random_list).lower()

# Global Variable Section (Variable initialize)
display = []
lives = 6

# Hiding the actual word
for i in word:
    display.append("_")
    
# Game loop
is_game_end = False
while not is_game_end:
    print(
        f"Hint : {hint(random_list=random_list)} and the length is {len(word)} and 3rd letter is {word[2]} ."
    )
    print(f"Word: {' '.join(display)}")
    guess = input("Guess a letter : ").lower()
    for position in range(len(word)):
        letter = word[position]
        if guess == letter:
            display[position] = letter

    if guess not in word:
        print(f"You guessed {guess}, that's not in this word.You lose a life.")
        lives -= 1
        if lives == 0:
            is_game_end = True
            print(f"You Lose, The Word was : {word}.")

        print(Hangman_art.stages[lives])

    if "_" not in display:
        is_game_end = True
        print(f"Yes The Word was {word}. You win")
