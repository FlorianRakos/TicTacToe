import re

print("")
print("Welcome to Tic Tac Toe!")

board = ["-","-","-",
        "-","-","-",
        "-","-","-",]

game_ongoing = True
winner = None
current_player = "X"



def display_board():
  print("")
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])
  print("")

def reset_board():
  global board
  board = ["-","-","-",
        "-","-","-",
        "-","-","-",]


def play_game():

  
  display_board()

  while game_ongoing :
    handle_turn(current_player)

    check_if_game_over()

    flip_player()

  # game has ended
  if winner == "X" or winner == "O":
    print(winner, " has won the game.")
  elif winner == None:
    print("Tie.")

  reset_game()


def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():
  global winner

  winner = check_combinations()
  

def check_combinations():
  global game_ongoing

  row_1 = [0,1,2]
  row_2 = [3,4,5]
  row_3 = [6,7,8]

  column_1 = [0,3,6]
  column_2 = [1,4,7]
  column_3 = [2,5,8]

  diagonal_1 = [0,4,8]
  diagonal_2 = [2,4,6]

  winning_combinations = [row_1, row_2, row_3, column_1, column_2, column_3, diagonal_1, diagonal_2 ]

  for combination in winning_combinations:

    if board[combination[0]] == board[combination[1]] == board[combination[2]] and board[combination[0]] != "-":
      game_ongoing = False
      return board[combination[0]]

  return


def check_if_tie():
  global game_ongoing

  if "-" not in board:
    game_ongoing = False

  return 


def flip_player():
  global current_player

  if current_player == "X":
     current_player = "O"
  else:
    current_player = "X"

  return


def handle_turn(current_player):
  print(current_player + "'s turn.")
 
  position = str(input("Choose a position from 1-9:"))

  valid = False
  
  while not valid:

    while not re.search("^[1-9]{1}$", position):
      position = input("Invalid Input. Choose a position from 1-9:")


    position = int(position) -1  

    if board[position] == "-":
      valid = True
    else:
      position = input("Position already marked. Go again.")


  board[position] = current_player
  display_board()


def reset_game():
  play_again = input("Press a Button to play again")

  global game_ongoing
  global winner
  global current_player

  game_ongoing = True
  winner = None
  current_player = "X"

  reset_board()
      
  play_game()

  

play_game()
