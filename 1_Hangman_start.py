
import random
import hangman_art
import hangman_words
print(hangman_art.logo)
end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

lives=6

#print(f'choosen words is {chosen_word}.')

#Creating blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

        
    if guess  not in chosen_word:
        lives=lives-1
        if lives==0:
            print("You lost")
            print(f"The correct solution was {hangman_words.chosen_word}")
            end_of_game=True
       
    #list to string conversion
    print(f"{' '.join(display)}")

    #check if the display doesnot contain '_'
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])