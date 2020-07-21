from blessings import Terminal
t = Terminal()
#====================================================
# Board class:
# Holds a 2d-array of tile objects
# and methods to interface with the game and other classes
#===========
class Board:
  #--------------------------------------------------
  def __init__(self,rows,cols):
    self.DARK_SQUARE = t.bright_blue
    self.LIGHT_SQUARE = t.white
    self.SELECTED_SQUARE = t.green
    self.rows = rows
    self.cols = cols
    self.tiles = [[None for c in range(self.cols)]for r in range(self.rows)]
  #--------------------------------------------------
  def makeBoard(self):
    for r,row in enumerate(self.tiles):
      for c,square in enumerate(row):
        sq_color = (self.LIGHT_SQUARE,self.DARK_SQUARE)[(r+c)%2]
        self.tiles[r][c] = Tile(self,(r,c),sq_color)
  #--------------------------------------------------
  def placePiece(self,piece,position):
    r,c = position
    self.tiles[r][c] = piece
  #--------------------------------------------------
  def setColors(self,dark,light,selected):
    self.DARK_SQUARE = dark
    self.LIGHT_SQUARE = light
    self.SELECTED_SQUARE = selected
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
  def __init__(self,board,position,color):
    self.board = board
    self.row,self.col = position
    self.color = color
    self.piece = None
  #--------------------------------------------------
#====================================================
# Piece class
# Holds the color, owner, position, and type of a piece
#===========
class Piece:
  SYMBOLS = {"pawn":"\u23fa", "king":"\u25c9"}
  #--------------------------------------------------
  def __init__(self,tile,owner,type="pawn"):
    self.owner = owner
    self.color = owner.color
    self.tile = tile
    self.type = type
  #--------------------------------------------------
  def getSymbol(self):
    return Piece.SYMBOLS[self.type]
  #--------------------------------------------------
  def move(self,position):
    pass