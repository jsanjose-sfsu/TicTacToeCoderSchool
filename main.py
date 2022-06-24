
# Constants aka, variables that should never be changed makes code, 
# more human readable. Also, if we need to make changes, we can change
# them in one spot rather than numerous others. 
CONST_PLAYER_1 = 1 # Constant number for Player 1
CONST_PLAYER_2 = 2 # Constant number for Player 2
# etc. 
CONST_NUM_OF_COLUMNS = 3
CONST_NUM_OF_ROWS = 3
CONST_NUM_OF_DIAGNOLS = 2

def getUserInformation():
  '''
  SHOW THIS
  '''
  # We ask for both player's names and record them. 
  # In order we should ask player 1 their name then player 2. 
  prompt_player1 = "Please enter player 1's name: "
  player1_name = input(prompt_player1)

  prompt_player2 = "Please enter player 2's name: "
  player2_name = input(prompt_player2)

  return player1_name, player2_name

def createGameGrid(): 
  '''
  SHOW THIS
  '''

  # What even is a grid? How do we create one using programming skills?
  # Think an array inside an array.
  
  gameGrid = [
              [0, 0, 0], 
              [0, 0, 0],
              [0, 0, 0]
  ]

  return gameGrid
  
def promptPlayerMove(list_of_players, player_turn): 
  '''
  SHOW THIS
  '''
  # Keep in mind we have to identify which player's turn it is. 
  prompt = None
  
  if(player_turn == 1): 
    prompt = "{} place your move: ".format(list_of_players[0])
  else: 
    prompt = "{} place your move: ".format(list_of_players[1])

  player_move = input(prompt)
    
  return player_move

def parsePlayerMove(player_move_input): 
  '''
  SHOW THIS
  '''
  # Definition of 'Parse': To analyze (a sentence) into its parts and describe the meaning. 
  # Now that we have the Player's input for moves we now have to 'make sense of them'
  # Or better yet, identify moves that are invalid. 
  # Quick.. think of moves that just dont make sense for a game like tictactoe
  # and how Player's will be inputting information. 
  player_move = player_move_input.replace(" ", "").split(',')

  # if the player enters more than 2 values then the player_move is invalid.
  if(len(player_move) != 2):
    return None
  else:
    # the player's move has to be a number and it has to fit in the game grid. 
    try: 
      player_move[0] = int(player_move[0])
      player_move[1] = int(player_move[1])
      if player_move[0] > 2 or player_move[1] > 2: 
        raise ValueError
    except ValueError:
      return None
      
  return player_move

def markLogicalGrid(logical_game_grid, list_of_players, player_move, player_turn): 
  '''
  SHOW THIS
  '''
  # Now that we've recieved proper input and parsed through the Player's input
  # we now have to mark the game grid where the Player specified.
  # NOTE; refer to the example of the grid below; 

  #    0 1 2
  # 0   | |1     Player 1 at (1,1)
  #   -------    Player 2 at (0,2)
  # 1   |2|
  #   ------- 
  # 2   | |

  # We also must think about situations where a box that is already been marked.
  x_coord = player_move[0]
  y_coord = player_move[1]
  
  if(logical_game_grid[x_coord][y_coord] > 0): 
    print("Box already marked by {}".format(list_of_players[player_turn - 1]))
  else: 
    logical_game_grid[x_coord][y_coord] = player_turn
  
def processTurn(list_of_players, logical_game_grid, player_turn):
  '''
  SHOW THIS
  '''
  # Let's think of how to actually process a turn when a player takes one.
  # They have to provide us some input on where to place their mark on the game grid.
  # ----- STEPS -----
  # 1) We have to prompt a user for their move and record it. 
  # 2) Make sure that their move is correct. 
  # 3) Mark the grid if their move makes sense. 
  player_move = None
  while(player_move is None):
    
    player_move_input = promptPlayerMove(list_of_players, player_turn)
    player_move = parsePlayerMove(player_move_input)
    
    if(player_move is None): 
      print("Invalid move. Try Again.")
    else: 
      # Apply the player's move to logical_game_grid
      markLogicalGrid(logical_game_grid, list_of_players, player_move, player_turn)

def markDisplayGrid(box_value):
  mark = None
  if box_value == CONST_PLAYER_1: 
    mark = 'X'
  elif box_value == CONST_PLAYER_2: 
    mark = 'O'
  else: 
    mark = ' '
  return mark 

def displayGameGrid(logical_game_grid): 
  # This just prints out the current state of our logical grid but instead of numbers they show for Xs Player 1 and Os for Player 2
  grid_display = f'''
{markDisplayGrid(logical_game_grid[0][0])}|{markDisplayGrid(logical_game_grid[0][1])}|{markDisplayGrid(logical_game_grid[0][2])}
-----
{markDisplayGrid(logical_game_grid[1][0])}|{markDisplayGrid(logical_game_grid[1][1])}|{markDisplayGrid(logical_game_grid[1][2])}
-----
{markDisplayGrid(logical_game_grid[2][0])}|{markDisplayGrid(logical_game_grid[2][1])}|{markDisplayGrid(logical_game_grid[2][2])}
'''
  print(grid_display)

def checkWinningRows(logical_game_grid, player_turn):
  # Checks ALL existing rows. 3 Of them
  isWinningCondition = False
  for i in range(0, CONST_NUM_OF_ROWS):
    if logical_game_grid[i][0] == player_turn \
    and logical_game_grid[i][1] == player_turn \
    and  logical_game_grid[i][2] == player_turn: 
      isWinningCondition = True
  return isWinningCondition

def checkWinningColumns(logical_game_grid, player_turn):
  # Checks ALL existing columns. 3 Of them
  isWinningCondition = False
  for i in range(0, CONST_NUM_OF_COLUMNS):
    if logical_game_grid[0][i] == player_turn \
    and logical_game_grid[1][i] == player_turn \
    and  logical_game_grid[2][i] == player_turn: 
      isWinningCondition = True
  return isWinningCondition
    
def checkWinningDiagnols(logical_game_grid, player_turn):
  # Checks ALL existing diagnols. 2 Of them. 
  if logical_game_grid[0][0] == player_turn \
    and logical_game_grid[1][1] == player_turn \
    and logical_game_grid[2][2] == player_turn:
      return True
  elif logical_game_grid[0][2] == player_turn \
    and logical_game_grid[1][1] == player_turn \
    and logical_game_grid[2][0] == player_turn: 
      return True
  else: 
    return False
  
def checkWinningCondition(logical_game_grid, player_turn): 
  '''
  SHOW THIS
  '''
  # What does it mean to actually win in tictactoe? 
  # Ask yourself, what do we need to check in order to define a winning situation. 

  # Inorder to identify a winner we have to check the following. 
  #   - check rows
  #   - check columns
  #   - check diagnols

  # if any of the rows, columns OR diagnols have Xs or Os that are filled 3 in a row. We dictate a winner. 
  # note to self; (EXPLAIN WITH PICTURES. 2-D grid looping through is hard to visualize by head alone.)
  if checkWinningRows(logical_game_grid, player_turn) \
    or checkWinningColumns(logical_game_grid, player_turn) \
    or checkWinningDiagnols(logical_game_grid, player_turn):
      return True
  else: 
    return False

def checkCatsGame(logical_game_grid):
  '''
  SHOW THIS
  '''
  # Not super important but, what given the concept of double for-loops
  # and us having to check a grid's boxes what does this do? 
  # Answer; it checks every box, from left to right, to see if there's a box that has
  # not been choosen as a move yet. 
  # Recall and show a draw situation below; 

  #    0 1 2
  # 0  X|O|X     This situation, no one wins. It's considered a tie or a CATS game.
  #   -------    Notice, all boxes are filled. Both Player 1 and Player 2 can no longer
  # 1  O|O|X     make moves. In all tie games, there is no free box.
  #   ------- 
  # 2  X|X|O

  # So if there's a free box, then it is not a tie game, otherwise if all boxes are taken
  # and there's still not a clear distinction of a winner then it is a tie. 
  for i in range(0, CONST_NUM_OF_ROWS):
    for j in range(0, CONST_NUM_OF_COLUMNS):
      if logical_game_grid[i][j] == 0: 
        return False # There still exist a free box.
  return True # It's a tie
  
def startGame(): 
  '''
  SHOW THIS
  '''
  # In order to start to play tictactoe we must consider quite a number of things, such as
  # - How do we know who's turn it is?
  # - How do we mark the "grid" through the computer? 
  # - What does it mean to actually win in this game?
  # - What other scenarios does this game face? Are Ties possible? (CATS game) 
  # Regardless we must do the following,
  # 1) Grab the information of the users who want to play
  # 2) Create the game "grid" for our players to play on
  # 3) Allow players to mark said "game grid"
  # 4) check to see if any players won, or if the game results in a tie. 

  # Our game set up. Read and predict what these do. 
  list_of_players = getUserInformation()
  logical_game_grid = createGameGrid()

  # The start of our game. 
  # NOTE: tictactoe is a turned based game. Meaning people take turns doing moves. 
  print("...game started.")
  isGameOver = False
  player_turn = CONST_PLAYER_1

  displayGameGrid(logical_game_grid)
  # What does this loop do? Guess by the names you see for the functions and variables. 
  while(isGameOver is False):
    
    processTurn(list_of_players, logical_game_grid, player_turn)
    displayGameGrid(logical_game_grid)

    isGameOver = checkWinningCondition(logical_game_grid, player_turn)

    if isGameOver is True: 
      print("Congratulations Player {}; {}, you've won! Exiting game"
            .format(player_turn, list_of_players[player_turn - 1]))
      break # Us ending the game once the game is over.

    isCatsGame = checkCatsGame(logical_game_grid)

    # Us resetting the game board when a tie or a CATS game occurs. 
    if isGameOver is False and isCatsGame is True:
      print("CATS game, resetting the grid... Touche~")
      logical_game_grid = createGameGrid()
      displayGameGrid(logical_game_grid)

    if(player_turn == CONST_PLAYER_1): 
      player_turn = CONST_PLAYER_2
    else: 
      player_turn = CONST_PLAYER_1

if __name__ == "__main__": 
  '''
  SHOW THIS
  '''
  # Prompt the players if they want to play. 
  # We check if users want to play if so; we start the game, 
  # we tell them goodbye or if improper input we tell them they provided an improper response. 
  # But how do we do we tell the computer how to do this?
  # ----- STEPS -----
  # 1) We send user a message to ask them if they want to play, and take in a response.
  #   - if they say yes then we 'start' the game for them. 
  #   - else if they say no, we simply end the program.
  #   - else the user may have given a bad response so we ask them again, yes or no. 
  
  while True:
    prompt = "Welcome to TicTacToe, would you like to play? Type Y for yes, N for no. "
    user_input = input(prompt)
    if user_input.lower() == "y": 
      print("Game starting...")
      # startGame() # unblock this when ready.
      print("Game Over")
    elif user_input.lower() == "n":
      print("...Goodbye")
      break
    else: 
      print("Improper Response. Try Again.")