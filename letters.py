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
    if letter == 'blank':
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
            Ns = self.Node()
            Nf = self.Node()
            self.node_list = [Ns,Nf]

        def dawg_generate(self):
            with open('//Users/glorisonlai/Documents/GitHub/OptimalScrabble/dict.rtf') as dictionary:
                for word in dictionary:
                    assert type(word) == str
                    word = word.split('\n')[0]
                    word = ''.join(e for e in word if e.isalpha())

                    print(word)

                    word = list(word)
                    cont = False
                    start,end = self.node_list[0],self.node_list[1]

                    """
                    Get letters Front -> Back already in dawg from Ns, while length > 1
                    """
                    while len(word) > 1:
                        out_letters = start.outgoing
                        letter = word[0]
                        
                        for edge in out_letters:
                            if letter == edge.Letter:
                                cont = True
                                word.pop(0)
                                start = edge.To 
                                break
                        if cont:
                            cont = False
                            continue
                        break

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
                                end = edge.From #What is the thing parsed
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
                        for edge in end.incoming:
                            if (word == edge.Letter):
                                cont = True
                                break
                        
                        if not(cont):
                            new_edge = self.Edge(word.pop(),start,end)
                            end.incoming.append(new_edge)
                            start.outgoing.append(new_edge)

                            self.edge_list.append(new_edge)

                    # start = Ns
                    # word = ''
                    # while start != Nf:
                    #     edge = start.outgoing[0]
                    #     word += edge.Letter
                    #     start = edge.To
                    # print(word)

if __name__ == '__main__':
    Dictionary = Dawg()
    Dictionary.dawg_generate()
    print('nodes = ' + str(len(Dictionary.node_list)))
    print('edges = ' + str(len(Dictionary.edge_list)))
    for edge in Dictionary.edge_list:
        print(edge.Letter)