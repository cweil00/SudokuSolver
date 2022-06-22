# Code for solving a sudoku puzzle using a backtracking algorithm
# Author: Chris Weil

def checkRow(r, num):
    row = b.getRow(r)
    if num in row:
        return False
    return True

def checkCol(c, num):
    col = b.getCol(c)
    if num in col:
        return False
    return True

def checkSquareGroup(r, c, num):
    s = b.getSquareGroup(r, c)
    if num in s:
        return False
    return True

def prevRC(r, c):
    if c > 0:
        newR = r
        newC = c-1
    else:
        if r > 0:
            newR = r-1
            newC = 8
        else:
            newR = -1
            newC = -1
    if b.getSquareTag(newR, newC) == 1:
        return prevRC(newR, newC)
    else:
        return newR, newC        

def nextRC(r, c):
    if c < 8:
        return r, c+1
    else:
        if r < 8:
            return r+1, 0
        else:
            return -1, -1

def solve():
    stack = []
    stack.append((0,0,1))
    while True:
        i = stack.pop()
        r = i[0]
        c = i[1]
        num = i[2]

        if r == -1 or c == -1:
            break
        if num > 9:
            b.setNumber(r, c, 0)
            r, c = prevRC(r, c)
            stack.append((r, c, b.getSquare(r, c)+1))
        elif b.getSquareTag(r, c) == 0:
            rf = checkRow(r, num)
            cf = checkCol(c, num)
            sf = checkSquareGroup(r, c, num)
            if rf and cf and sf:
                b.setNumber(r, c, num)
                r, c = nextRC(r, c)
                stack.append((r, c, 1))
            else:
                stack.append((r, c, num+1))
        else:
            r, c = nextRC(r, c)
            stack.append((r, c, 1))
    return None

def runSolver(t):
    global b
    b = t
    solve()
    print(b.toString())