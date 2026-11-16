"""Game of Sticks.

Implementation of the Game of Sticks, including an AI that learns the game,
either by playing against a human, or by pre-training against another AI.

Author: <INSERT YOUR FULL NAME AND USD EMAIL HERE>
"""

import random


def get_player_selection(player_number, sticks_left):
    """To Do: Add a proper docstring for this function."""

    return -1 # To Do: Replace this line with your implementation.


def player_vs_player(num_sticks):
    """To Do: Add a proper docstring for this function."""

    pass # To Do: Replace this line with your implementation.


def main():
    """Main function that orchestrates the playing of the game.
    
    The program will ask how many sticks to start with and which mode
    they player want.
    """
    print("Welcome to the Game of Sticks!")
    num_sticks = int(input("How many sticks are there on the table initially (10-100)? "))

    player_vs_player(num_sticks)


# DO NOT MODIFY ANYTHING BELOW THIS LINE!!!

if __name__ == "__main__":
    main()

