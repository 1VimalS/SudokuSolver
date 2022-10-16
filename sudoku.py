import pyautogui as pag 
import time

# main board
board = []



# driver function to solve board
def gui_driver():
  time.sleep(4)
  solved_board = []
  str_solved = []
  for i in range(9):
    solved_board.append(board[i])
  for rows in board:
    for cols in rows:
      str_solved.append(str(cols))
  counter = []

  for i in str_solved:
    
    pag.press(i)
    pag.hotkey('right')
    
    counter.append(i)
    if len(counter) % 9 == 0:
      pag.hotkey('down')
      pag.hotkey('left')
      pag.hotkey('left')
      pag.hotkey('left')
      pag.hotkey('left')
      pag.hotkey('left')
      pag.hotkey('left')
      pag.hotkey('left')
      pag.hotkey('left')

# function to print board on terminal neatly
def print_board():
  for i in range(len(board)):
    if i % 3 == 0 and i != 0:
      print("-------------------------")
    for j in range(len(board[0])):
      if j % 3 == 0 and j != 0:
        print(" | ", end="")
      if j == 8:
        print(board[i][j])
      else:
        print(str(board[i][j]) + " ", end="")

# boolean check if guess is valid in solve algorithm
def valid(guess, row, col):
  row_vals = board[row]
  if guess in row_vals:
    return False
  
  col_vals = [board[i][col] for i in range(len(board))]
  if guess in col_vals:
    return False
  
  box_vals = []
  if row >= 0 and row <= 2:
    if col >= 0 and col <= 2:
      box_vals = [board[i][j] for i in range(3) for j in range(3)]
     

      if col >= 3 and col <= 5:
        box_vals = [board[i][j+3] for i in range(3) for j in range(3)]
       

        if col >= 6 and col <= 8:
          box_vals = [board[i][j+6] for i in range(3) for j in range(3)]            

  if row >= 3 and row <= 5:
    if col >= 0 and col <= 2:
      box_vals = [board[i+3][j] for i in range(3) for j in range(3)]
      

    if col >= 3 and col <= 5:
      box_vals = [board[i+3][j+3] for i in range(3) for j in range(3)]
            

    if col >= 6 and col <= 8:
      box_vals = [board[i+3][j+6] for i in range(3) for j in range(3)]
            
  
  if row >= 6 and row <= 8:
    if col >= 0 and col <= 2:
      box_vals = [board[i+6][j] for i in range(3) for j in range(3)]
            

    if col >= 3 and col <= 5:
      box_vals = [board[i+6][j+3] for i in range(3) for j in range(3)]
            

    if col >= 6 and col <= 8:
      box_vals = [board[i+6][j+6] for i in range(3) for j in range(3)]
            
  if guess in box_vals:
    return False
  return True    

# solve the sudoku puzzle and run the driver
def solve():
  
  for row in range(len(board)):
    for col in range(len(board[0])):
      if board[row][col] == 0:

  
        for i in range(1, 10):
          if valid(i, row, col):
            board[row][col] = i
            solve()
              
          board[row][col] = 0
        return
  gui_driver()
  input("Hit Enter to Print Solution")
  print_board()


# main function
def main():

  # input values
  while True:
    row = list(input("Row: "))
    rows = []

    for i in row:
      rows.append(int(i))
    board.append(rows)
    print(board)
    if len(board) == 9:
      break
    
  solve()

if __name__ == "__main__":
  main()