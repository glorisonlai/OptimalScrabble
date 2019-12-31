from letters import *
from board import Board
import string
import letters
import copy

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
                options_hori,options_vert = [],[]
                if check_tile.Letter == None:
                    r,l_substring,r_substring = x-1,'',''
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
                    r,l_substring,r_substring = y-1,'',''
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
                else:
                    self.board.xy([x,y]).Maybe = None
                print(str([x,y]) + ', ' + str(self.board.xy([x,y]).Maybe))

    def extend_hori_words(self,word,stack,hand,pos):
        words,stack = [],[]
        if self.dict.is_valid(word):
            words.append(word)
        
        if board.xy(length,row).Letter != None:
            stack.append(board.xy(length,row).Letter)
        elif board.xy(length,row).Maybe != None:
            stack.append(e for e in board.xy(length,row).Maybe)
        else:
            stack.append(e for e in hand)
        

        return words+self.extend_hori_words(word,new_stack)


    def generate_hori_words(self,letter,anchor):
        row,anchor_col = anchor[0],anchor[1]
        word,valid = '',False
        for start in range(anchor_col):
            length = start
            hand = copy.copy(self.rank)
            if board.xy(length,row).Letter != None:
                stack.append(board.xy(length,row).Letter)
            elif board.xy(length,row).Maybe != None:
                stack.append(e for e in board.xy(length,row).Maybe)
            else:
                stack.append(e for e in hand)
            while len(stack) > 0:
                if board.xy(length,row):
                    pass


            for length in range(start,self.width):
                for hand_letter in self.rank:
                    hand = copy.copy(self.rank)
                    
                    if self.dict.is_valid(word):
                        self.final_words.append( [(start,row),True,word] )
                

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
