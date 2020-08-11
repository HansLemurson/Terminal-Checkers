import random
from board import *
#======================================================
class Player:
  #----------------------------------------------------
  def __init__(self,name,color):
    self.name = name
    self.color = color  
  #----------------------------------------------------
#======================================================
from blessings import Terminal
t = Terminal()
#------------------------------------------------------
class Game:
  DARK_SQUARE = t.on_black #Dark Gray
  LIGHT_SQUARE = t.on_blue #t.on_color(124) #Dark Red
  P1_PIECES = [(0,1),(0,3),(0,5),(0,7),(1,0),(1,2),(1,4),(1,6),(2,1),(2,3),(2,5),(2,7)]
  P2_PIECES = [(7,0),(7,2),(7,4),(7,6),(6,1),(6,3),(6,5),(6,7),(5,0),(5,2),(5,4),(5,6)]
  #----------------------------------------------------
  def __init__(self,player1,player2,size=8):    
    self.player1 = player1
    self.player2 = player2
    self.players = [player1,player2]
    self.size = size
    self.board = self.newGame()
  #----------------------------------------------------
  def newGame(self):
    board = Board(self.size,self.size)
    for pos in Game.P1_PIECES:
      # rpiece = random.choice(["pawn","king"])
      #Test a random mix of Kings and Pawns to compare pieces
      board.placePiece(Piece(self.player1,"pawn"),pos)
    for pos in Game.P2_PIECES:
      # rpiece = random.choice(["pawn","king"])
      board.placePiece(Piece(self.player2,"pawn"),pos)
    return board
  #----------------------------------------------------
  #----------------------------------------------------
  def printBoard(self,row_offset,col_offset):
    for r,row in enumerate(self.board.squares):
      for c,square in enumerate(row):
        location = t.move(r+row_offset,2*c+col_offset)
        if square.is_dark:
          square_color = Game.DARK_SQUARE  
        else: 
          square_color = Game.LIGHT_SQUARE

        if square.piece:
          piece = square.piece.getSymbol()
          piece_color = square.piece.getColor()
        else:
          piece = " "
          #Should only show if something went wrong
          piece_color = t.bright_magenta 

        data_string = f'{location}{square_color}{piece_color}{piece:2}'
        print(data_string+t.normal)


  #----------------------------------------------------
  #----------------------------------------------------

  
    