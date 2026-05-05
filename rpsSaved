"""
Program name: rpsSaved.py
Date/version/revision: 1.0
Programmer(s): Jessie Conn
This program allows the user to play Rock, Paper, Scissors against the computer.
It tracks wins, losses, and ties, and saves this data using the shelve module
so that stats persist between program runs.

Original code from Chapter 3 of "Automate the Boring Stuff with Python" included
in this repository as RockPaperScissors
"""

import random
import sys
import shelve

print('ROCK, PAPER, SCISSORS')

# Open shelve file
save_file = shelve.open('rps_save')

# Load saved stats or default to 0
wins = save_file.get('wins', 0)
losses = save_file.get('losses', 0)
ties = save_file.get('ties', 0)

while True:  # The main game loop
    print(f'{wins} Wins, {losses} Losses, {ties} Ties')

    while True:  # Player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        player_move = input('> ').lower()

        if player_move == 'q':
            # Save before quitting
            save_file['wins'] = wins
            save_file['losses'] = losses
            save_file['ties'] = ties
            save_file.close()
            print('Game saved. Goodbye.')
            sys.exit()

        if player_move in ['r', 'p', 's']:
            break

        print('Type one of r, p, s, or q.')

    # Display player move
    if player_move == 'r':
        print('ROCK versus...')
    elif player_move == 'p':
        print('PAPER versus...')
    elif player_move == 's':
        print('SCISSORS versus...')

    # Computer move
    move_number = random.randint(1, 3)
    if move_number == 1:
        computer_move = 'r'
        print('ROCK')
    elif move_number == 2:
        computer_move = 'p'
        print('PAPER')
    else:
        computer_move = 's'
        print('SCISSORS')

    # Determine result
    if player_move == computer_move:
        print('It is a tie!')
        ties += 1
    elif (player_move == 'r' and computer_move == 's') or \
         (player_move == 'p' and computer_move == 'r') or \
         (player_move == 's' and computer_move == 'p'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1

    # Save stats after each round
    save_file['wins'] = wins
    save_file['losses'] = losses
    save_file['ties'] = ties
