#from Collections import counter
from board import Board
import letters

class Generator:
    width, height = Board.board_cols, Board.board_rows

    class POI:
        def __init__(self):
            self.options=[]

    def __init__(self,letters):
        self.rank = letters
        self.final_words = []

    def cross_check(self,board):
        

    def valid_anchors(self,board):
        anchors = []
        anchors += cross_check(board)
        for row in board:
            print(row)

    def generate_words(self, letters):
        pass

if __name__ == "__main__":
    game = Board()
    game.update_state([ [(1,1),True,"at"],[(2,2),False,"be"] ])
    game.show_board()

    rank =['b','c']
    generate = Generator(rank)
    generate.valid_anchors()
