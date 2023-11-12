import random
from wordlist import wordlist

MAXIMUM_GUESSES = 6
NUMBER_OF_LETTERS = 5

def process_guess(the_answer, the_guess):
    clue = ['-', '-', '-', '-', '-']
    answer_flag = [False, False, False, False, False]
    #print(answer_flag)

    # Exact match loop
    for i, _ in enumerate(the_answer):
        if the_guess[i] == the_answer[i]:
            clue[i] = 'G'
            answer_flag[i] = True
    
    # Present, but out of position loop
    for i, _ in enumerate(the_guess):
        if clue[i] == '-': # No exact match from first loop
            for j, _ in enumerate(the_answer):
                if the_guess[i] == the_answer[j] and not answer_flag[j]:
                    clue[i] = 'Y'
                    answer_flag[j] = True
                    break # End the loop
    for letter in guess:
        print(letter, end = " ")
    print('')
    for i in range(NUMBER_OF_LETTERS):
        print(clue[i], end=" ")
    print('')
    return the_answer == the_guess

# choose a word
answer = random.choice(wordlist)

guess_count = 0
correct_guess = False

while guess_count < MAXIMUM_GUESSES and not correct_guess:
    guess = input('input 5 letter word and hit enter: ')
    if guess not in wordlist:
        print(f'{guess} not a valid word')
        continue
    guess_count += 1
    print(f'guess # {guess_count}')
    print('')
    correct_guess = process_guess(answer, guess)
    if guess_count == MAXIMUM_GUESSES and not correct_guess:
        print(f'the word was {answer}')
