# Demo of a mills game board creation created by myself during my education at Softuni!

from colorama import Fore
from collections import deque
from copy import deepcopy

import positions


# Custom exceptions:
class InvalidChoice(Exception):
    pass

class PositionTaken(Exception):
    pass
    

# Function to print the board numeration: 
def print_board_positions():
    print("Board positions:")
    
    num = 97
    for i in range(SIZE):
        if i != 3:
            board_copy[i][i] = chr(num)
            num += 1
    
    for i in range(SIZE):
        if i != 3:        
            board_copy[i][3] = chr(num)
            num += 1
     
    for i in range(SIZE):
        if i != 3:       
            board_copy[i][SIZE - i - 1] = chr(num)
            num += 1
            
    for i in range(SIZE):
        if i != 3:
            board_copy[3][i] = chr(num)
            num += 1
        
    for row in range(SIZE):
        for col in range(SIZE):
            print(board_copy[row][col], end=" ")
            
        print()


# Function to print the board state: 
def print_board_state():
    print("Board state:")
    for row in range(SIZE):
        for col in range(SIZE):
            print(board[row][col], end=" ")
        
        print()
        
        
# Function to print all the boards info:
def print_board_info():
    print_board_positions()
    print()
    print_board_state()
        
   
# Function to create the players:  
def create_player(i=None):
    player_name = input(f"Player {i}, please enter your name: ")
    
    if i == "one":
        player_symbol = "W"
        print(f"{player_name} plays with red mills ({Fore.RED + 'W' + Fore.RESET})")
    else:
        player_symbol = "B"
        print(f"{player_name} plays with blue mills ({Fore.BLUE + 'B' + Fore.RESET})")
        
    return player_name, player_symbol


# Function to place player's symbol:
def place_symbol(pos):
    if players[0][1] == "W":  
        board[positions.POSITIONS[pos][0]][positions.POSITIONS[pos][1]] = Fore.RED + "W" + Fore.RESET
    else:
        board[positions.POSITIONS[pos][0]][positions.POSITIONS[pos][1]] = Fore.BLUE + "B" + Fore.RESET
        
# Function to check if a line of mills is formed:        
def check_for_line():
    pass


# Create the playing board:
SIZE = 7

board = [[' '] * SIZE for _ in range(SIZE)]

for i in range(SIZE):
    board[i][i] = "O"
    board[i][SIZE - i - 1] = "O"
    board[3][i] = "O"
    board[i][3] = "O"
    
board[3][3] = " "

#Create a deepcopy of the board:
board_copy = deepcopy(board)

player_one = create_player("one")
player_two = create_player("two")

players = deque([player_one, player_two])

print_board_info()

print()
print("Fill the board with your mills to start the game:")

turns = 0
while turns < 18:
    try:
        player_choice = input(f"{players[0][0]}, choose where to place your mill(a-x): ")
        
        if ord(player_choice) < 97 or ord(player_choice) > 120:
            raise InvalidChoice
        elif board[positions.POSITIONS[player_choice][0]][positions.POSITIONS[player_choice][1]] != "O":
            raise PositionTaken
        
    except InvalidChoice:
        print("Invalid postion chosen! Choose again: ")
        continue
    except PositionTaken:
        print("Position is already taken! Choose another one: ")
        continue
    
    place_symbol(player_choice)
    print_board_info()
    
    turns += 1
    players.rotate()
