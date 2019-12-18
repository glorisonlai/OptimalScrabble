def scores(letter):
    if letter == 'a':
        return 1
    if letter == 'b':
        return 3
    if letter == 'c':
        return 3
    if letter == 'd':
        return 2
    if letter == 'e':
        return 1
    if letter == 'f':
        return 4
    if letter == 'g':
        return 2
    if letter == 'h':
        return 4
    if letter == 'i':
        return 1
    if letter == 'j':
        return 8
    if letter == 'k':
        return 5
    if letter == 'l':
        return 1
    if letter == 'm':
        return 3
    if letter == 'n':
        return 1
    if letter == 'o':
        return 1
    if letter == 'p':
        return 3
    if letter == 'q':
        return 10
    if letter == 'r':
        return 1
    if letter == 's':
        return 1
    if letter == 't':
        return 1
    if letter == 'u':
        return 1
    if letter == 'v':
        return 4
    if letter == 'w':
        return 4
    if letter == 'x':
        return 8
    if letter == 'y':
        return 4
    if letter == 'z':
        return 10
    if letter == '_':
        return 0

class Dawg:
    class Node:
        def __init__(self,incoming = None,outgoing = None):
            self.incoming = []
            self.outgoing = []

    class Edge:
        def __init__(self,letter,From = None,To = None):
            self.From = From
            self.To = To
            self.Letter = letter

    def __init__(self):
        self.edge_list = []
        self.Ns = self.Node()
        self.Nf = self.Node()
        self.node_list = [self.Ns,self.Nf]

    def dawg_generate(self):
        with open('//Users/glorisonlai/Documents/GitHub/OptimalScrabble/dict.rtf') as dictionary:
            for word in dictionary:
                try:
                    assert type(word) == str
                    word = word.split('\n')[0]
                    assert word.isalpha()
                    word = word.lower()
                except AssertionError:
                    print(type(word),word)

                word = list(word)
                cont = False
                start,end = self.node_list[0],self.node_list[1]

                """
                Get letters Front -> Back already in dawg from Ns, while length > 1
                """
                # while len(word) > 1:
                #     out_letters = start.outgoing
                #     letter = word[0]

                #     for edge in out_letters:
                #         if letter == edge.Letter:
                #             cont = True
                #             word.pop(0)
                #             start = edge.To
                #             break
                #     if cont:
                #         cont = False
                #         continue
                #     break

                """
                Get letters Back -> Front already in dawg from Nf, while length > 0
                """
                while len(word) > 1:
                    in_letters = end.incoming
                    letter = word[-1]

                    for edge in in_letters:
                        if letter == edge.Letter:
                            cont = True
                            word.pop()
                            end = edge.From
                            break
                    if cont:
                        cont = False
                        continue
                    break

                """
                Put in nodes/edges from breaknode 0 -> 1
                """
                while len(word) > 1:
                    new_node = self.Node()
                    new_edge = self.Edge(word.pop(0),start,new_node)

                    new_node.incoming.append(new_edge)
                    start.outgoing.append(new_edge)
                    start = new_node

                    self.node_list.append(new_node)
                    self.edge_list.append(new_edge)

                if len(word) == 1:
                    #Checksum for repeat words
                    for edge in start.outgoing:
                        if (word[0] == edge.Letter) and (edge.To == end):
                            cont = True
                            break

                    if not(cont):
                        new_edge = self.Edge(word.pop(),start,end)
                        end.incoming.append(new_edge)
                        start.outgoing.append(new_edge)

                        self.edge_list.append(new_edge)

    def traverse_dawg(self,index,string,node):
        if node == self.Nf and index == len(string):
            return True
        elif index >= len(string):
            return False
        else:    
            for edge in node.outgoing:
                if edge.Letter == string[index]:
                    if self.traverse_dawg(index+1,string,edge.To):
                        return True

    def is_valid(self,string):
        try:
            if not string.isalpha():
                raise TypeError
        except TypeError:
            print("invalid input: %s" % string)
            
        string = string.lower()
        index = 0

        return bool(self.traverse_dawg(index,string,self.Ns))

if __name__ == '__main__':
    Dictionary = Dawg()
    Dictionary.dawg_generate()
    print(Dictionary.Ns.outgoing)
    print(Dictionary.is_valid("a"))