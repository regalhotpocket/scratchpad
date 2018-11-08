class Board:
    def __init__(self):
        self.tiles = [['-','-','-'],['-','-','-'],['-','-','-']]
        #self.xturn = True
    def __repr__(self):
        return ""+self.tiles[0][0] + "|" +self.tiles[1][0] + "|" +self.tiles[2][0] +"\n" + self.tiles[0][1] + "|" + self.tiles[1][1] + "|" + self.tiles[2][1] +"\n" + self.tiles[0][2] + "|" + self.tiles[1][2] + "|" + self.tiles[2][2] +"\n"
    def print_board(self):
        print(self)
    def add_token(self, token, x, y):
        if self.tiles[x][y] == '-':
            self.tiles[x][y] = token
            #self.tiles[x][y] = 'x' if self.xturn else 'o'
            #self.xturn = not self.xturn
            return True
        else:
            return False
    def full(self):
        for row in self.tiles:
            for tile in row:
                if tile == '-':
                    return False
        return True
    def ai(self):
        for x in range(3):
            for y in range(3):
                if self.tiles[x][y] == '-':
                    self.add_token('o', x, y)
                    return
        raise Exception('No move') 
b = Board()
b.print_board()
b.print_board()
print(b.full())
for a in range(10):
    b.ai()
    b.print_board()
print(b.full())

