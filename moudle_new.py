# in the name of ALLAH

class Minimax:
    def __init__(self, bot, opponet):

        self.bot = bot
        self.opponent = opponet

        # This function returns true if there are moves
        # remaining on the board. It returns false if
        # there are no moves left to play.

    def generate_plugin(self, l, cols):
        return [l[i:i + cols] for i in range(0, len(l), cols)]

    def generate_1d(self, first, sec):
        if first == 0:
            return sec
        elif first == 1:
            return ((first*2)+sec+1)
        else:
            return ((first*3)+sec)
        # return [j for sub in list for j in sub]

    def generate_2d(self, boor):

        new_list = [shape if (type(shape) == str) else '_' for shape in boor]
        return self.generate_plugin(new_list, 3)

    def isMovesLeft(self, board):

        for i in range(3):
            for j in range(3):
                if (board[i][j] == '_'):
                    return True
        return False
    
    def reset(self, bot, opponet):

        # Python3 program to find the next optimal move for a player
        self.bot = bot
        self.opponent = opponet

    # This is the evaluation function as discussed

    def evaluate(self, b):

        # Checking for Rows for X or O victory.
        for row in range(3):
            if (b[row][0] == b[row][1] and b[row][1] == b[row][2]):
                if (b[row][0] == self.bot):
                    return 10
                elif (b[row][0] == self.opponent):
                    return -10

        # Checking for Columns for X or O victory.
        for col in range(3):

            if (b[0][col] == b[1][col] and b[1][col] == b[2][col]):

                if (b[0][col] == self.bot):
                    return 10
                elif (b[0][col] == self.opponent):
                    return -10

        # Checking for Diagonals for X or O victory.
        if (b[0][0] == b[1][1] and b[1][1] == b[2][2]):

            if (b[0][0] == self.bot):
                return 10
            elif (b[0][0] == self.opponent):
                return -10

        if (b[0][2] == b[1][1] and b[1][1] == b[2][0]):

            if (b[0][2] == self.bot):
                return 10
            elif (b[0][2] == self.opponent):
                return -10

        # Else if none of them have won then return 0
        return 0

    # This is the minimax function. It considers all
    # the possible ways the game can go and returns
    # the value of the board

    def minimax(self, board, depth, isMax):
        score = self.evaluate(board)

        # If Maximizer has won the game return his/her
        # evaluated score
        if (score == 10):
            return score

        # If Minimizer has won the game return his/her
        # evaluated score
        if (score == -10):
            return score

        # If there are no more moves and no winner then
        # it is a tie
        if (self.isMovesLeft(board) == False):
            return 0

        # If this maximizer's move
        if (isMax):
            best = -1000

            # Traverse all cells
            for i in range(3):
                for j in range(3):

                    # Check if cell is empty
                    if (board[i][j] == '_'):

                        # Make the move
                        board[i][j] = self.bot

                        # Call minimax recursively and choose
                        # the maximum value
                        best = max(best, self.minimax(board,
                                                      depth + 1,
                                                      not isMax))

                        # Undo the move
                        board[i][j] = '_'
            return best

        # If this minimizer's move
        else:
            best = 1000

            # Traverse all cells
            for i in range(3):
                for j in range(3):

                    # Check if cell is empty
                    if (board[i][j] == '_'):

                        # Make the move
                        board[i][j] = self.opponent

                        # Call minimax recursively and choose
                        # the minimum value
                        best = min(best, self.minimax(
                            board, depth + 1, not isMax))

                        # Undo the move
                        board[i][j] = '_'
            return best

    # This will return the best possible move for the player

    def findBestMove(self, board):
        bestVal = -1000
        bestMove = (-1, -1)

        # Traverse all cells, evaluate minimax function for
        # all empty cells. And return the cell with optimal
        # value.
        for i in range(3):
            for j in range(3):

                # Check if cell is empty
                if (board[i][j] == '_'):

                    # Make the move
                    board[i][j] = self.bot

                    # compute evaluation function for this
                    # move.
                    moveVal = self.minimax(board, 1, False)

                    # Undo the move
                    board[i][j] = '_'

                    # If the value of the current move is
                    # more than the best value, then update
                    # best/
                    if (moveVal > bestVal):
                        bestMove = (i, j)
                        bestVal = moveVal

        # print("The value of the best Move is :", bestVal)
        # print()
        bestMove = self.generate_1d(bestMove[0], bestMove[1])
        # bestMove = self.generate_1d(bestMove)
        # bestMove_num = self.generate_1d(bestMove)

        return bestMove
    
