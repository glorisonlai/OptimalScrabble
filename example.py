from board import Board
from generator import *
import letters

game = Board()
game.update_state([ [(1,1),True,"at"] ])
game.show_board()

rank =['b','c']
generate = Generator(rank)
generate.valid_anchors(game.board_state)
