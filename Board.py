import numpy as np

class Board:
    def __init__(self):
        self.board = np.zeros((9,9))
        self.tags = np.zeros((9,9))
    
    def setNumber(self, r, c, num):
        self.board[r][c] = num
        return None
    
    def setNumberWithTag(self, r, c, num):
        self.tags[r][c] = 1
        self.setNumber(r, c, num)
        return None
    
    def getSquare(self, r, c):
        return self.board[r][c]
    
    def getSquareTag(self, r, c):
        return self.tags[r][c]

    def getRow(self, r):
        return self.board[r]
    
    def getCol(self, c):
        col = []
        for row in self.board:
            col.append(row[c])
        return np.array(col)
    
    def getSquareGroup(self, r, c):
        if r < 3: #top three squares
            row = 0
        elif r < 6: #middle three squares
            row = 3
        else: #bottom three squares
            row = 6
        if c < 3:
            col = 0
        elif c < 6:
            col = 3
        else:
            col = 6
        square = self.board[row][col:col+3]
        square = np.append(square, self.board[row+1][col:col+3])
        square = np.append(square, self.board[row+2][col:col+3])
        return square
    
    def getBoard(self):
        return self.board
    
    def getTags(self):
        return self.tags

    def toString(self):
        toReturn = ""
        rowCount = 0
        for row in self.board:
            colCount = 0
            for col in row:
                toReturn += str(int(col))
                if colCount == 2 or colCount == 5:
                    toReturn += " | "
                elif colCount != 8:
                    toReturn += " "
                colCount += 1
            if rowCount != 8:
                toReturn += "\n"
            if rowCount == 2 or rowCount == 5:
                toReturn += "------+-------+------\n"
            rowCount += 1
        return toReturn

