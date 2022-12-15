import numpy as np

class State:
    def __init__(self,board):
        #print("state created")
        self.board = board.copy()
        self.playerID = self.evalID()
        self.eval = self.evalBoard()
        self.children = []

    def generateChildren(self):
        ans = []
        board = self.board
        playerID = self.evalID()
        choices = np.nonzero(board == 0)
        tempBoard = board.copy() 
        numChoices = len(choices[0])
        for i in range(numChoices):
            tempBoard = board.copy()
            tempBoard[choices[0][i], choices[1][i]] = playerID
            ans.append(State(tempBoard))
        self.children = ans
            
        
    def evalID(self):
        board = self.board
        if np.count_nonzero(board == 1) > np.count_nonzero(board == -1):
            return -1
        else:
            return 1

    def evalBoard(self):
        board = self.board 
        playerID = self.playerID
        ans = -50 if playerID != self.evalID() else 0
        x2 = 0
        x1 = 0
        o2 = 0
        o1 = 0
        # rows
        for row in board:
            blanks = np.count_nonzero(row == 0)
            enemy = np.count_nonzero(row == -1 )
            ally = np.count_nonzero(row == 1)
            if blanks == 2 and enemy == 1:
                o1 +=1
            elif blanks == 2 and ally == 1:
                x1 +=1
            elif blanks == 1 and enemy == 2:
                o2 +=1
            elif blanks == 1 and ally == 2:
                x2 += 1
            elif enemy == 3:
                return -1000
            elif ally == 3:
                return 1000
        # columns
        for row in board.T:
            blanks = np.count_nonzero(row == 0)
            enemy = np.count_nonzero(row == -1 )
            ally = np.count_nonzero(row == 1)
            if blanks == 2 and enemy == 1:
                o1 +=1
            elif blanks == 2 and ally == 1:
                x1 +=1
            elif blanks == 1 and enemy == 2:
                o2 +=1
            elif blanks == 1 and ally == 2:
                x2 += 1
            elif enemy == 3:
                return -1000
            elif ally == 3:
                return 1000
        # northwest-diag
        diags = [np.diag(board),np.diag(np.fliplr(board))]
        for diag in diags:
            blanks = np.count_nonzero(diag == 0)
            enemy = np.count_nonzero(diag == -1)
            ally = np.count_nonzero(diag == 1)
            if blanks == 2 and enemy == 1:
                o1 +=1
            elif blanks == 2 and ally == 1:
                x1 +=1
            elif blanks == 1 and enemy == 2:
                o2 +=1
            elif blanks == 1 and ally == 2:
                x2 += 1
            elif enemy == 3:
                return -1000
            elif ally == 3:
                return 1000
        ans+= (3 * x2 + x1) - (3 * o2 + o1)
        return ans
