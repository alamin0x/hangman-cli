import random
import Hangman_Word_list as HWL
import Hangman_art as art

# <== Random Word from Word_list ==>
random_category = random.choice(list(HWL.categories.keys()))
word = random.choice(HWL.categories[random_category]).lower()  # Convert to lowercase for case insensitivity

def hints():
    for category, items in HWL.categories.items():
        if word in [item.lower() for item in items]:  # Convert all items to lowercase for matching
            return f"It's one of the {category.capitalize()}"

display = ["-" for _ in word]
guessed_letters = set()  # Store guessed letters
game_On = True
life = 6

print(art.logo)
while game_On:
    print(f"\nWord : {' '.join(display)}")
    print(f"{hints()}. It has {len(word)} letters, and the last letter is '{word[-1]}'")
    print(f"Lives Remaining: {life}")
    
    guess = input("\nGuess a Letter: ").lower()
    
    if guess in guessed_letters:
        print("\n⚠️ You've already guessed this letter! Try another one.")
        continue
    
    guessed_letters.add(guess)
    
    if guess in word:
        for position in range(len(word)):
            if guess == word[position]:
                display[position] = guess
    else:
        life -= 1
        print(art.stages[life])
        print(f"\nWrong guess!")
        if life == 0:
            print(f"Game Over!Better luck next time! ☠️\nThe word was : {word}")
            game_On = False
    
    if "-" not in display:
        print("\n🎉 WINNER! You guessed the word correctly! 🎉")
        game_On = False
