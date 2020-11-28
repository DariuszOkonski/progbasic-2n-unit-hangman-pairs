import time
import os

picture7 = """
    ||=====|
    |/     0
    ||   -{ }-
    ||    / \\
    || GAME OVER  
"""
picture6 = """
    ||=====|
    |/     0
    ||   -{ }-
    ||    / 
    ||    
"""
picture5 = """
    ||=====|
    |/     0
    ||   -{ }-
    ||    
    ||    
"""
picture4 = """
    ||=====|
    |/     0
    ||   -{ }
    ||    
    ||    
"""
picture3 = """
    ||=====|
    |/     0
    ||    { }
    ||  
    ||    
"""
picture2 = """
    ||=====|
    |/     0
    ||   
    ||   
    ||    
"""
picture1 = """
    ||=====|
    |/    
    ||   
    ||    
    ||    
"""

def console_clear():
    os.system('cls')
hangman_list = [picture1, picture2, picture3, picture4, picture5, picture6, picture7]

def draw_single_hangman(index):
    console_clear()
    print(hangman_list[index])


def draw_hangman(hangman_list):

    for item in hangman_list:
        console_clear()
        print(item)
        time.sleep(2)

draw_hangman(hangman_list)