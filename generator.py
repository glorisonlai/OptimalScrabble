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

                    if l_substring == '' and r_substring == '':
                        options_hori = None
                    else:
                        for letter in list(string.ascii_lowercase):
                            if self.dict.is_valid(l_substring+letter+r_substring):
                                options_hori.append(letter)

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

                    if l_substring == '' and r_substring == '':
                        options_vert = None
                    else:
                        for letter in list(string.ascii_lowercase):
                            if self.dict.is_valid(l_substring+letter+r_substring):
                                options_vert.append(letter)

                    if options_hori == None and options_vert == None:
                        self.board.xy([x,y]).Maybe = None
                    elif options_hori == None:
                        self.board.xy([x,y]).Maybe = options_vert
                    elif options_vert == None:
                        self.board.xy([x,y]).Maybe = options_hori
                    else: self.board.xy([x,y]).Maybe = [e for e in options_hori if e in options_vert]

    def generate_hori_words(self,letter,anchor):
        row = anchor[1]
        word,valid = '',False
        for start in range(self.width):
            for length in range(start,self.width):
                pass

    def generate_vert_words(self,anchor):
        pass

     def rank_options(self,arr):
        pass

    def get_anchors(self,board):
        self.final_words = []
        for row in range(len(board[0])):
            for col in range(len(board)):
                tile = self.board.xy([col,row])
                if tile.Letter != None: 
                    self.generate_hori_words(tile.Letter,[row,col])
                    self.generate_vert_words(tile.Letter,[row,col])
                elif tile.Maybe != None:
                    for letter in tile.Maybe:
                        self.generate_hori_words(letter,[row,col])
                        self.generate_vert_words(letter,[row,col])
        self.rank_options(self.final_words)
        return

if __name__ == "__main__":
    rank = ['b','c']
    generate = Generator(rank)

    generate.board.update_state([ [(1,1),True,"at"],[(2,2),False,"be"] ])
    #generate.board.update_state([ [(1,1),True,"at"] ])

    generate.board.show_board()
    generate.cross_check()

    # generate.get_anchors()
