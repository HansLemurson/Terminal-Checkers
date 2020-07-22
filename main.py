from blessings import Terminal
from game import Game, Player

t = Terminal()
print(t.green+"Python Operational")
print(t.normal)

def printBoard(board,row_offset=2,col_offset=4):
  for r,row in enumerate(board):
    for c,square in enumerate(row):
      location = t.move(r+row_offset,c*2+col_offset)
      square_color = t.on_bright_blue if (r+c)%2==1 else t.on_white
      piece = "\u23fa"
      piece_color = t.bright_red
      text = f"{location}{piece_color}{square_color}{piece:2}{t.normal}"
      print(text)


# TEST_BOARD = [
#   [0,0,0,0,0,0,0,0],
#   [0,0,0,0,0,0,0,0],
#   [0,0,0,0,0,0,0,0],
#   [0,0,0,0,0,0,0,0],
#   [0,0,0,0,0,0,0,0],
#   [0,0,0,0,0,0,0,0],
#   [0,0,0,0,0,0,0,0],
#   [0,0,0,0,0,0,0,0],
# ]

# printBoard(TEST_BOARD)
p1 = Player("Alice",t.red)
p2 = Player("Bob", t.color(0))
g = Game(p1,p2)
g.printBoard(4,4)
