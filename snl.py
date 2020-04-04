#!/usr/bin/env python3
import random

# Board values are the next square the player will go, even if it is the same square.
board = [0, 1, 19, 3, 4, 13, 6, 7, 8, 9, 27, 11, 12, 13, 33, 15, 73, 0, 18, 19, 20, 36, 22, 23, 24, 9, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 4, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 5, 51, 52, 35, 54, 0, 75, 57, 58, 22, 77, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 27, 75, 76, 77, 78, 79, 97, 81, 44, 83, 59, 85, 86, 90, 88, 47, 90, 24, 92, 93, 94, 95, 86, 97, 62, 99]
playerLocations = [0 for p in range(2)]

# Check if either of these are empty
if not board or not playerLocations: quit(-1)

# Check if anyone player is at the last square of the board
# Multiple players may win in the same turn
while not any(playerLocation == board[-1] for playerLocation in playerLocations):
    # loop over the "index" of each player
    for playerIndex in range(len(playerLocations)):
        playerRoll = random.randint(1, 6)
        playerNext = playerLocations[playerIndex] + playerRoll
        print(f'P{playerIndex}: {playerLocations[playerIndex]} --({playerRoll})-> {playerNext}')
        # Player must land within the board to move
        if playerNext > board[-1]:
            print(f'P{playerIndex}: skipping turn')
        else:
            if playerNext > board[playerNext]:
                print(f'P{playerIndex}: {playerNext} --(snake)-> {board[playerNext]}')
            elif board[playerNext] > playerNext:
                print(f'P{playerIndex}: {playerNext} --(ladder)-> {board[playerNext]}')
            playerNext = board[playerNext]
            playerLocations[playerIndex] = playerNext
            # Player must land exactly on the final square to win
            if playerNext == board[-1]:
                print(f'P{playerIndex}: wins!')

# Really helpful if there's like 10,000 players
print('Final Results:')
for playerIndex in range(len(playerLocations)):
    if playerLocations[playerIndex] == board[-1]:
        print(f'\tP{playerIndex} Won')
