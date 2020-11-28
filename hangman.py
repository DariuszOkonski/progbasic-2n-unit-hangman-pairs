import os
import random

# Pobieranie państwa z pliku
def read_file(path):
    with open(path) as f:
        lines = f.readlines()
    return lines

def get_word_to_guess():
    path = "countries-and-capitals.txt"

    countries = read_file(path)

    single_country = random.choice(countries)
    guess = single_country.split(' ')[0]

    return guess

def get_letter():
    
    while True:
        letter = input('Give a letter: ').lower()

        if(letter == 'quit'):
            return "Game Over"

        if(len(letter) == 1):
            return letter
        else:
            print("Wrong input, try again")


def guess_board(word):
    word_length = len(word)
    board = ('_' * word_length)
    return board
    
def if_input_correct(guess, board, letter):
    guess_list = list(guess)
    print(guess_list)

    board_list = list(board)
    print(board_list)


    index = 0
    for item in guess_list:
        if(item.lower() == letter):
            board_list[index] = item
        index += 1

    return board_list

    # tu skończyliśmy



# wywołanie funkcji play
def play(guess, lives):
    board = guess_board(guess)
    
    letter = get_letter()

    while True:
        board = if_input_correct(guess, board, letter)

    




# guess = get_word_to_guess()
play('Codecool', 7)
# print(ord('0'))
# print(ord('9'))


















# guess = get_word_to_guess()
# print(guess)


# def play(word, lives):
#     print("Hello world")



#   0
# -{ }-
#  / \

# gr = [
#     ['','','0','',''],
#     ['-','{','','}','-'],
#     ['','/','','\','']
# ]