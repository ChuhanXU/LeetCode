
# 1.find unassigned grid
# 2.go through 123456789
# 3 check row check col and check square
# O(9^m)
# backtracking
# go through all the number 123456789 still can't find
# return False and go back to last step

class Solution:

    def solveSudoku(self,board):
        row,col = self.findEmpty(board)
        if row==-1 and col == -1:
            return board
        for num in ["1","2","3","4","5","6","7","8","9"]:
            if self.isSafe(row,col,num):
                self.board[row][col]=num
                if self.solveSudoku(board):
                    return True
                self.board[row][col]="."
        return False


    def findEmpty(self,board):
        for row in range(9):
            for col in range(9):
                if self.board[row][col]==".":
                    return row,col
        return -1,-1


    def isSafe(self,row,col,num):
        # (2,2)
        boxrow = row-row%3
        boxcol = col-col%3
        if self.checkCol(row,num) and self.checkRow(col,num) and self.checksquare(boxrow,boxcol,num):
            return True
        return False

    def checkRow(self,row,num):
        for col in range(9):
            if self.board[row][col]==num:
                return False
        return True

    def checkCol(self,col,num):
        for row in range(9):
            if self.board[row][col]==num:
                return False
        return True

    def checksquare(self,row,col,num):
        for row in range(row,row+3):
            for col in range(col,col+3):
                if self.board[row][col]==num:
                    return False
        return True





