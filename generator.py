from letters import *
from board import Board
import string
import letters

class Generator:
    width, height = Board.board_cols, Board.board_rows

    def __init__(self,letters):
        self.dict = Dawg()
        self.dict.dawg_generate()
        self.board = Board()
        self.rank = letters
        self.final_words = []

    def cross_check(self):
        for y in range(self.height):
            for x in range(self.width):
                check_tile = self.board.xy([x,y])
                if check_tile.Letter == None:     
                    r,l_substring,r_substring = x-1,'',''
                    options_hori,options_vert = [],[]
                    #generate horizontal check
                    while (r in range(self.width) and self.board.xy([r,y]).Letter != None):
                        l_substring = self.board.xy([r,y]).Letter + l_substring
                        r -= 1
                    r = x+1
                    while (r in range(self.width) and self.board.xy([r,y]).Letter != None):
                        r_substring += self.board.xy([r,y]).Letter
                        r += 1
                    #check with list of alpha with dict and put valid words into options_hori
                    for letter in list(string.ascii_lowercase):
                        if self.dict.is_valid(l_substring+letter+r_substring):
                            options_hori.append(l_substring+letter+r_substring)

                    #repeat for vert
                    r = y-1
                    while (r in range(self.height) and self.board.xy([x,r]).Letter != None):
                        l_substring = self.board.xy([x,r]).Letter + l_substring
                        r -= 1
                    
                    r = y+1
                    while (r in range(self.height) and self.board.xy([x,r]).Letter != None):
                        r_substring += self.board.xy([x,r]).Letter
                        r += 1
                    #check with list of alpha with dict and put valid words into options_hori
                    for letter in list(string.ascii_lowercase):
                        if self.dict.is_valid(l_substring+letter+r_substring):
                            options_vert.append(l_substring+letter+r_substring)

                    if len(options_hori) == 0 or len(options_vert) == 0:
                        self.board.xy([x,y]).Maybe = max(options_hori,options_vert)
                    else: self.board.xy([x,y]).Maybe = [e for e in options_hori if e in options_vert]

    def valid_anchors(self,board):
        anchors = []
        anchors += cross_check(board)
        for row in board:
            print(row)

    def generate_words(self, letters):
        pass

if __name__ == "__main__":
    rank = ['b','c']
    generate = Generator(rank)
    
    #generate.board.update_state([ [(1,1),True,"at"],[(2,2),False,"be"] ])
    generate.board.update_state([ [(1,1),True,"at"] ])
    
    generate.board.show_board()
    generate.cross_check()

    # generate.valid_anchors()
