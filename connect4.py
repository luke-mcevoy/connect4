#Luke McEvoy
#I pledge my honor that I have abided by the Stevens Honor System


class Board(object):

    def __init__(self, width=7, height=6):
#initializes the object
        self.width = width
        self.height = height
        self.Board = []
        for x in range(self.height):
            self.Board.append([])
            for y in range(self.width):
                self.Board[x].append(' ')
        #print(self.Board)

    def __str__(self):
#returns a string
        string = ''
        for x in self.Board:
            string += '|' + '|'.join(x) + '|\n'
        string += '-' + '-' * self.width * 2 + '\n'
        string += ' ' + ' '.join(str(x) for x in range(self.width))
        return string
        
    def allowsMove(self, col):
#This method should return True if the calling Board object can
#allow a move into column c
        if col > self.width or col < 0 or self.Board[0][col] != ' ':
            return False
        return True
            
    def addMove(self, col, ox):
#This method should add an ox checke
        if self.allowsMove(col):
            for i in list(reversed(range(self.height))):
                if self.Board[i][col] == ' ':
                    self.Board[i][col] = ox
                    break
                
    def setBoard(self, move_string):
#This method helps you (and us!) to test your Connect-Four Board class
        nextCh = 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X':
                nextCh = 'O'
            else:
                nextCh == 'X'

    def delMove(self, col):
#This method should do the "opposite" of addMove.
        if self.allowsMove(col):
            return
        else:
            self.Board[0][col] = ' '

    def winsFor(self, ox):
#This method should return True if the given checker, 'X' or 'O', held
#in ox, has won the calling Board. It should return False otherwise
        result = 1
        for row in list(reversed(range(self.height))):
            for col in range(self.width):
                if ox not in self.Board[row][col]:
                    continue
                if row > 2:
                    for i in range(1,4):
                        if self.Board[row-i][col] == ox:
                            result = result + 1
                        else:
                            result = 1
                            break
                    if result == 4:
                        return True
                if col > 2:
                    for i in range(1,4):
                        if self.Board[row][col-i] == ox:
                            result = result + 1
                        else:
                            result = 1
                            break
                        if result == 4:
                            return True
                if col > 2 and row > 2:
                    for i in range(1,4):
                        if self.Board[row-i][col-i] == ox:
                            result = result + 1
                        else:
                            result = 1
                            break
                        if result == 4:
                            return True
                if row > 2 and col < self.width - 3:
                    for i in range(1,4):
                        if self.Board[row-i][col+i] == ox:
                            result = result + 1
                        else:
                            result = 1
                            break
                        if result == 4:
                            return True

    def hostGame(self):
#This is a method that, when called from a connect four board object, will
#run a loop allowing the user(s) to play a game. See below for an example user interface.
        print('Welcome to Connect Four Game')
        print('')
        while True:
            var = input('Xs choice: ')
            self.addMove(int(var),'X')
            print(self)
            if self.winsFor('X'):
                print('X player won')
                break
            var = input('Os choice: ')
            self.addMove(int(var), 'O')
            print(self)
            if self.winsFor('O'):
                print('O player won')
                break
                    
                    

