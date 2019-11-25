class Board:
    board_rows = 4
    board_cols = 4 #4x4 board

    class Tile:
        def __init__(self,letter = None):
            self.Letter = letter
            self.Maybe = []

    def __init__(self):
        self.board_state = [[self.Tile() for i in range(self.board_cols)] for j in range(self.board_rows)]
        self.state = []

    def xy(self,pos):
        return self.board_state[pos[1]][pos[0]]

    def show_board(self):
        for row in self.board_state:
            print_line = row
            for i in range(len(row)):
                tile = print_line[i]
                if tile.Letter == None:
                    print_line[i] = ' '
                else:
                    print_line[i] = tile.Letter
            print(print_line)

    def update_board(self):
        new_word = self.state[-1]
        pos = list(new_word[0])
        hori = new_word[1]
        text = list(new_word[2])

        while len(text) > 0: #Repeat until word is done
            self.board_state[pos[1]][pos[0]] = self.Tile(text.pop(0)) #Remove first item of word
            if hori == True:
                pos[0] += 1
            else: pos[1] += 1

    def update_state(self,args): 
        for arg in args:
            try:
                if not(type(arg[0]) == tuple and type(arg[1]) == bool and type(arg[2]) == str):
                    raise TypeError("invalid arg types: %s" % [type(arg[0]),type(arg[1]),type(arg[2])])
                self.state.append(arg)
                self.update_board()
            except (TypeError):
                pass


if __name__ == "__main__":
    game = Board()
    game.update_state([ [(1,1),True,"at"],[(1,1),False,"be"] ])
    game.show_board()
