import random




stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

from hangman_words import word_list
chosen_word = random.choice(word_list)
print(chosen_word)

display = []
word_length = len(chosen_word)
space = "_"
lives = 6
end_of_game = False


for each_letter in chosen_word:
        display += space

print(display)
while not end_of_game:
    guess = input("Guess a letter ").lower()
    if guess in display:
        print(f"You already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print(stages[lives])
        print(f"You guessed {guess}")
        
        lives -= 1
    if lives == 0:
        end_of_game = True
        print(f"You lose, word is {chosen_word.upper()}")
    print(f"{' '.join(display)}")

    if space not in display:
        end_of_game = True
        print("You win")


    


    


    
    





    
    
    
    


  







