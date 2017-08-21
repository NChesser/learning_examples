import random
import itertools

class Player(object):
    def __init__(self):
        self.position = 0
        self.double_count = 0
    
    def dice_roll(self, sides):
        d1 = random.randrange(1,sides+1)
        d2 = random.randrange(1,sides+1)

        if d1 == d2:
            self.double_count += 1
        else:
            self.double_count = 0

        return d1 + d2

class Square(object):    
    def __init__(self, name):
        self.name = name
        self.landed_on = 0

p = Player()
board_squares = "GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 JAIL C1 U1 C2 C3 R2 D1 CC2 D2 D3 FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 G2J G1 G2 CC3 G3 R4 CH3 H1 T2 H2"
board = [Square(s) for s in board_squares.split()]

def go_to_square(square):
    if square != "Nothing":
        for s in board:
            if s.name == square:
                p.position = board.index(s)

def go_to_next(index, square):
    while square not in board[index%len(board)].name:
        index += 1
    p.position = index%len(board)

def go_back_3(position):
    if position - 3 < 0:
        p.position = position + len(board) - 3
    else: p.position = position-3
    

community_chest = "GO JAIL"
chance = "GO JAIL C1 E3 H2 R1 NEXTR NEXTR NEXTU BACK3"

cc = ["Nothing" for i in range (14)]
cc.append("GO")
cc.append("JAIL")
ch = [i for i in chance.split()]

while len(ch) < 16:
    ch.append("Nothing")

random.shuffle(cc)
random.shuffle(ch)

def pick_up_card(card):
    c = card.pop(0)
    if c[:4] == "NEXT":
        go_to_next(p.position, c[4:])
    elif c[:4] == "BACK":
        go_back_3(p.position) 
    else:
        go_to_square(c)
    card.append(c)

def game(dice_sides):
    rolls = 0
    while rolls < 1000000:
        p.position += p.dice_roll(dice_sides)
        p.position %= len(board)
        
        if board[p.position].name == "G2J" or p.double_count == 3:
            p.position = 10
        elif board[p.position].name[:2] == "CH":
            pick_up_card(ch)
        elif board[p.position].name[:2] == "CC":
            pick_up_card(cc)

        board[p.position].landed_on += 1
        rolls += 1
    
    for s in board:
        print(str(s.name) + " " + str(board.index(s)) +  " " + str((s.landed_on/rolls)*100))

game(4)



