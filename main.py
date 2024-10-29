import words_fetcher
import random
from create_full_list import create_full_list


def congratulate_user():
    print(f"Congratulations, you won! your words: {guesses}")


def is_game_over():
    return guessed == words_to_win or errors == ERRORS_TO_LOSE


guessed = 0
errors = 0

guesses = []

ERRORS_TO_LOSE = 3

words = words_fetcher.fetch_words(min_letters=9, max_letters=9)
word = words[random.randrange(0, len(words))]
full_list = create_full_list(ok_words=words_fetcher.fetch_words(min_letters=3, max_letters=9),word=word)
words_to_win = min(5, len(full_list))

print(f"Can you make up {words_to_win} words from letters in word provided by me?")
print(f"Your word is '{word}'")


while not is_game_over():
    guess = input("Your next take: ")
    if guess in full_list and guess not in guesses:
        guessed += 1
        guesses.append(guess)
        if guessed == words_to_win:
            congratulate_user()
            exit()
        print(f"That's right! {words_to_win - guessed} to go")
    else:
        errors += 1
        if errors < 3:
            print(f"Oops :( No such word, you have {ERRORS_TO_LOSE - errors} lives more")
        else:
            break
