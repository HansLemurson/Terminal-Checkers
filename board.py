# from blessings import Terminal
# t = Terminal()
#====================================================
# Board class:
# Holds a 2d-array of tile objects
# and methods to interface with the game and other classes
#===========
class Board:
  #--------------------------------------------------
  def __init__(self,rows,cols):
    self.rows = rows
    self.cols = cols
    self.squares = [[None for c in range(self.cols)]for r in range(self.rows)]
    self.makeBoard()
    # self.pieces = []
  #--------------------------------------------------
  def makeBoard(self):
    '''Fills the squares grid with new Tile objects''' 
    for r,row in enumerate(self.squares):
      for c,square in enumerate(row):
        is_dark = ((r+c)%2 == 1)
        self.squares[r][c] = Tile(self,(r,c),is_dark)
  #--------------------------------------------------
  def placePiece(self,piece,position):
    r,c = position
    self.squares[r][c].piece = piece
    # self.pieces.append(piece)
  #--------------------------------------------------
  def inBoard(self,position):
    row,col = position
    row_good = (0 <= row < self.rows)
    col_good = (0 <= col < self.cols)
    return row_good and col_good
  #--------------------------------------------------
#====================================================
# Tile class:
# Stores color and piece data for a square in the board
#===========
class Tile:
  #--------------------------------------------------
  def __init__(self,board,position,is_dark):
    self.board = board
    self.row,self.col = position
    self.is_dark = is_dark
    self.piece = None
  #--------------------------------------------------
#====================================================
# Piece class
# Holds the color, owner, position, and type of a piece
#===========
class Piece:
  SYMBOLS = {"pawn":"\u23fa", "king":"\u25c9"}
  #--------------------------------------------------
  def __init__(self,owner,type="pawn"):
    self.owner = owner
    self.type = type
  #--------------------------------------------------
  def getSymbol(self):
    return Piece.SYMBOLS[self.type]
  #--------------------------------------------------
  def getColor(self):
    return self.owner.color
  #--------------------------------------------------
  def move(self,position):
    pass
