import speech_recognition as sr

from collections import deque
from pyfiglet import figlet_format
from termcolor import colored, cprint


# Function to get player's name:
def get_players_name(i):
    while True:
        with sr.Microphone() as source:
            r = sr.Recognizer()
            print(f"Player {i}, please say your name: ")

            audio = r.record(source, duration=3)
            print("Recognizing...")
            
            try:
                return r.recognize_google(audio)
            except sr.exceptions.UnknownValueError:
                print("Could not recognize speech! Say your name again!")
                

# Function to get player's symbol and create the player:   
def create_player(i):    
    player_name = get_players_name(i)
    
    if i == 2:
        player_symbol = SYMBOLS.pop()
        return [player_name, player_symbol]
    
    while True:
        player_symbol = input(f"{player_name}, please choose 'X' or 'O': ").upper()
        
        if player_symbol not in SYMBOLS:
            print(f"{player_name}, choose a valid symbol!")
        else:
            SYMBOLS.remove(player_symbol)
            return [player_name, player_symbol]
        
        
# Function to print board state:
def print_board(start=False):
    if start:
        print("This is how the board looks like:")
        [print(f"| {' | '.join(row)} |") for row in board]
        
        for row in range(SIZE):
            for col in range(SIZE):
                board[row][col] = " "
    else:
        [print(f"| {' | '.join(row)} |") for row in board]
        
        
# Function to check if a win has happened:
def check_for_win():
    player_name, player_symbol = players[0]

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(SIZE)])
    second_diagonal_win = all([board[i][SIZE - i - 1] == player_symbol for i in range(SIZE)])

    row_win = any([all(player_symbol == pos for pos in row) for row in board])
    col_win = any([all(board[r][c] == player_symbol for r in range(SIZE)) for c in range(SIZE)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print_board()
        print(f"{player_name} won!")
        color_win_path(player_symbol, first_diagonal_win, second_diagonal_win, row_win, col_win)
        
        while True:
            play_again = input("Do you want to play again(Yes/No)? ").upper()
            
            if play_again == "YES":
                start_game()
            elif play_again == "NO":
                print("Goodbye!")
                exit(0)
            else:
                print("Invalid user input!")
        
        
# Function to color the winning path and restart/end the program:
def color_win_path(symbol, *possible_win_paths):
    first_diagonal_win, second_diagonal_win, row_win, col_win = possible_win_paths
    
    if first_diagonal_win:
            for i in range(SIZE):
                board[i][i] = colored(board[i][i], 'green')
            print_board()
    elif second_diagonal_win:
        for i in range(SIZE):
            board[i][SIZE - i - 1] = colored(board[i][SIZE - i - 1], 'green')
        print_board()
    elif row_win:
        for row in range(SIZE):
            if all([pos == symbol for pos in board[row]]):
                for col in range(SIZE):
                    board[row][col] = colored(board[row][col], 'green')
                break
        print_board()
    elif col_win:
        for col in range(SIZE):
            if all([board[r][col] == symbol for r in range(SIZE)]):
                for row in range(SIZE):
                    board[row][col] = colored(board[row][col], 'green')
                break
        print_board()
        
        
# Function for player to choose position:
def choose_position():
    global turns
    
    while True:
        try:
            position = int(input(f"{players[0][0]}, choose a free board spot: "))
            
            row = (position - 1) // SIZE
            col = (position - 1) % SIZE
        except ValueError:
            print("Invalid player input! Enter your position again(Number required): ")
            continue
        
        if not 1 <= position <= SIZE * SIZE:
            print("Chosen position not in range(1-9)! Choose again: ")
        elif board[row][col] != ' ':
            print("Spot already taken! Choose again: ")
        else:
            turns += 1
            place_symbol(row, col)
        
        
# Function to place player's move:
def place_symbol(row, col):
    board[row][col] = players[0][1]
    
    check_for_win()
    print_board()
    
    if turns == SIZE * SIZE:
        print("Draw!")
        exit(0)
        
    players.rotate()
                
              
# Main function to start the game:
def start_game():
    game_name = figlet_format("Tic-Tac-Toe game", font = "slant", width = 200)
    color = "yellow"
    
    cprint(game_name, color)
    
    player_one = create_player(1)
    player_two = create_player(2)
    
    print(f"{player_one[0]} plays with {player_one[1]}")
                
    print(f"{player_two[0]} plays with {player_two[1]}")
    
    players.append(player_one)
    players.append(player_two)
    
    print_board(start=True)
    choose_position()
    

SYMBOLS = ['X', 'O']

SIZE = 3
turns = 0

board = [[str(i), str(i+1), str(i+2)] for i in range(1, SIZE * SIZE + 1, SIZE)]

players = deque()

start_game()