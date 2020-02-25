from letters import *
from board import Board
import string
import letters
import copy

# def generate_combinations_aux(word,ls,length):
#     if length == 0:
#         return word
    
# def generate_combinations(ls,length):
    if length == 0:
        return [""]
    result = []
    for item in ls:
        result += generate_combinations_aux(item,ls.remove(item),length-1)

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable) #immutable
    n = len(pool) 
    r = n if r is None else r #length of yield
    if r > n: 
        return
    
    indices = list(range(n)) #Field mapper
    cycles = list(range(n, n-r, -1)) #No. cycles left for i'th int
    yield tuple(pool[i] for i in indices[:r]) #print original config
    
    while n: #if arr len > 0
        for i in reversed(range(r)): #Change back elements first

            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1] #Swap positions
                cycles[i] = n - i #Reset no. of cycles left for i'th int
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                print(indices)
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

class Generator:
    dict_tree = Dawg.dawg_generate
    width, height = Board.board_cols, Board.board_rows

    def __init__(self,letters):
        self.dict = Dawg()
        self.dict.dawg_generate()
        self.board = Board()
        self.rank = letters
        self.final_words = []

    def cross_check(self,board):
        width,height = self.width, self.height
        for y in range(height):
            for x in range(width):
                check_tile = board.xy([x,y])
                options_hori,options_vert = [],[]
                if check_tile.Letter == None:
                    r,l_substring,r_substring = x-1,'',''
                    #generate horizontal check
                    while board.space_left([r,y]):
                        l_substring = board.letter([r,y]) + l_substring
                        r -= 1
                    r = x+1
                    while board.space_right([r,y]):
                        r_substring += board.letter([r,y])
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
                    while board.space_up([x,r]):
                        l_substring = board.letter([x,r]) + l_substring
                        r -= 1

                    r = y+1
                    while board.space_down([x,r]):
                        r_substring += board.letter([x,r])
                        r += 1
                    #check with list of alpha with dict and put valid words into options_hori

                    if l_substring == '' and r_substring == '':
                        options_vert = None
                    else:
                        for letter in list(string.ascii_lowercase):
                            if self.dict.is_valid(l_substring+letter+r_substring):
                                options_vert.append(letter)

                    #validate options
                    if options_hori == None and options_vert == None:
                        board.xy([x,y]).Maybe = None
                    elif options_hori == None:
                        board.xy([x,y]).Maybe = options_vert
                    elif options_vert == None:
                        board.xy([x,y]).Maybe = options_hori
                    else: board.xy([x,y]).Maybe = [e for e in options_hori if e in options_vert]
                else:
                    board.xy([x,y]).Maybe = None

    # def create_pre_words(col,row,rank):
    #     for length in range(col,-1,-1):
    #             start,valid = length,False
    #             pos = [start,row]
    #             if board.space_left(pos) or start == 0: #does not connect to letters on its left
    #                 hand = copy.copy(rank)
    #                 while start in range(col): #includes no preword 
    #                     max_preword_len = col-start
    #                     #Generate all combinations of self.rank
    #                     for preword_len in range(max_preword_len+1):
    #                         prewords += (e for e in permutations(hand,preword_len))
    #             else: break

    def finish_word(self,anchor,word,rank):
        board = self.board
        

    def create_pre_words(self,start,goal,rank,letter,word):
        if start[0] == goal[0]:
            word = word + letter
            if self.dict_tree.partial_valid("word"):
                return self.finish_word(anchor,word,rank)
            else:
                return []
        else:
            for tile of rank:
                if self.dict_tree.partial_valid(word+tile):
                    col,row = start[0]-1,start[1]
                    self.create_pre_words([col,row],goal,rank.remove(tile),letter,word+tile)

    #DICTIONARY MUST EXIST
    def generate_hori_words(self,letter,anchor,rank):
        col,row = anchor[0],anchor[1]
        board = self.board
        prewords = []
        #Either attach to word, or generate pre-words
        if board.space_left(anchor): #Create all valid pre-words, and for each, finish word
            start_col, start = col, anchor
            while board.space_left(start):
                prewords += self.create_pre_words(start,anchor,rank,letter,"")
                start_col -= 1
                start = [start_col,row]
        else: #preword exists
            start_col,preword = col,""
            while not(board.space_left([start_col,row])):
                start_col -= 1
                preword = board.Letter([start_col,row]) + preword
            word = preword + letter
            if dict_tree.partial_valid(word):
                self.finish_word(anchor,word,rank)
            else:
                return


    def generate_vert_words(self,letter,anchor,rank):
        pass

    def rank_options(self,arr):
        pass

    def get_anchors(self,board):
        self.final_words = []
        for y in range(self.height):
            for x in range(self.width):
                pos = [x,y]
                tile = board.xy(pos)
                #tile is letter
                if (board.space_left(pos) or board.space_right(pos)): #Only if next tile is free
                    if (tile.Letter): 
                        self.generate_hori_words(tile.Letter,pos,self.rank)
                    elif tile.Maybe != None:
                        for letter in tile.Maybe:
                            if letter in self.rank:
                                self.generate_hori_words(letter,pos,self.rank.remove(letter))
                if (board.space_up(pos) or board.space_down(pos)):
                    if (tile.Letter):
                        self.generate_vert_words(tile.Letter,pos,self.rank)
                    elif tile.Maybe:
                        for letter in tile.Maybe:
                            if letter in self.rank:
                                self.generate_vert_words(letter,pos,self.rank.remove(letter))
        self.rank_options(self.final_words)
        print(self.final_words)
        return

if __name__ == "__main__":
    rank = ['b','c']
    generate = Generator(rank)

    generate.board.update_state([ [(0,1),True,"cat"],[(2,2),False,"be"] ])
    #generate.board.update_state([ [(1,1),True,"at"] ])

    generate.board.show_board()
    generate.cross_check(generate.board)

    generate.get_anchors(generate.board.board_state)
