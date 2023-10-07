import operator
from collections import deque
from colorama import Fore


# Create a custom Exception to handle invalid user input:
class ValueNotInRange(Exception):
    pass


# Function for printing the board state after each move:
def print_board():
    print("Current board state: ")
    [print(f"[ {', '.join(row)} ]") for row in board]
    print()


# Function for creating the players:
def create_players(i=None):
    player_name = input(f"Player {i}, enter name: ")

    while True:
        try:
            player_digit = int(input("Enter your lucky digit to play with(1-9): "))

            if player_digit < 1 or player_digit > 9:
                raise ValueNotInRange
        except ValueError:
            print(Fore.RED + "Oops... Non-integer type entered!" + Fore.RESET + " Please enter a valid digit: ")
            continue
        except ValueNotInRange:
            print(Fore.RED + "Oops... Integer not in range entered!" + Fore.RESET + " Enter a valid digit: ")
            continue

        if i == "one":
            return player_name, Fore.RED + f"{player_digit}" + Fore.RESET
        elif i == "two":
            return player_name, Fore.BLUE + f"{player_digit}" + Fore.RESET


# Function for placing player's digit on the board:
def place_player_digit():
    row = 0

    while row != ROWS and board[row][player_col] == "0":
        row += 1

    board[row-1][player_col] = player_symbol

    return row - 1


# Function to check if the board index is valid:
def check_is_valid_index(row, col):
    return 0 <= row < ROWS and 0 <= col < COLS


# Function to get player's digit count for possible win:
def get_player_digits_count(row, col, dir_x, dir_y, operator_func):
    curr_count = 0

    for i in range(1, 4):
        new_row = operator_func(row, dir_x * i)
        new_col = operator_func(col, dir_y * i)

        if not check_is_valid_index(new_row, new_col):
            break

        if board[new_row][new_col] != player_symbol:
            break

        curr_count += 1

    return curr_count


# Fucntion to check if there is a win:
def check_for_win(row, col):
    for x, y in directions:
        count = get_player_digits_count(row, col, x, y, operator.add) + get_player_digits_count(row, col, x, y, operator.sub) + 1

        if count >= 4:
            return True

    if draw_counter == ROWS * COLS:
        print_board()
        print("Draw!")
        exit(0)

    return False


# Main code:
while True:
    ROWS, COLS = 6, 7 #by default

    draw_counter = 0

    board = [["0"] * COLS for _ in range(ROWS)] #create the board for play

    players = [[], []]

    players[0] = create_players(i="one")
    players[1] = create_players(i="two")

    print()

    # Print player's info:
    print(f"Player one: {'-> '.join(str(x) for x in players[0])}")
    print(f"Player two: {'-> '.join(str(x) for x in players[1])}")
    
    print()

    turns = deque(players)

    # Initialise board directions:
    directions = (
        (-1, 0),  # up
        (0, 1),   # right
        (-1, -1), # up-left
        (-1, 1),  # up-right
    )

    win = False
    while not win:
        print_board()

        player_name, player_symbol = turns[0]

        try:
            player_col = int(input(f"{player_name}, choose a column: ")) - 1

            if player_col < 0 or player_col > COLS:
                raise ValueNotInRange
        except (ValueError, ValueNotInRange):
            print(Fore.RED + f"Select a valid number in the range (1-{COLS})" + Fore.RESET)
            continue

        if board[0][player_col] != "0":
            print(Fore.RED + "No empty spaces on that column!" + Fore.RESET + " Choose another one!")
            continue

        row = place_player_digit()
        
        draw_counter += 1
        
        win = check_for_win(row, player_col)

        # Switch players positions after each move
        turns.rotate()

    # If win:
    print_board()
    print(Fore.GREEN + f"Player {turns[1][0]} wins!" + Fore.RESET)
    
    # Save winning player's name in a file:
    with open("first_workshop/player_wins.txt", "a") as file:
        file.write(f"{turns[1][0]} ")

    # Ask players for another game:
    play_again = input("Do you you want to play again" + "(" + Fore.GREEN + "Yes" + Fore.RESET + "/" + Fore.RED + "No" + Fore.RESET + ")? ").upper()

    if play_again == "YES":
        continue
    elif play_again == "NO":
        print("Goodbye!")
        break
    
#Print the final results of the game streak:
results = []

try:
    with open("first_workshop/player_wins.txt", "r") as file:
        results = file.readline().split()        
except FileNotFoundError:
    print(Fore.RED + "Game failed..." + Fore.RESET)
    exit(0)
    
total_wins_first_player = results.count(players[0][0])
total_wins_second_player = results.count(players[1][0])
        
print("Game summary:")
print(f"{players[0][0]} has {total_wins_first_player} wins.")
print(f"{players[1][0]} has {total_wins_second_player} wins.")

if total_wins_first_player > total_wins_second_player:
    print(Fore.GREEN +  f"{players[0][0]} is the final winner" + Fore.RESET)
elif total_wins_first_player < total_wins_second_player:
    print(Fore.GREEN +  f"{players[1][0]} is the final winner" + Fore.RESET)
else:
    print(Fore.YELLOW + "Draw" + Fore.RESET)

file = open("first_workshop/player_wins.txt", "r+")

file.seek(0)
file.truncate()

file.close()