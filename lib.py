
from moudle_new import Minimax


positions = ['O', 'X', 'X',
             4, 5, 'X',
             7, 8, 'O']
# board = [0, 1, 2,
#          3, 4, 5,
#          6, 7, 8]

# for num in board:
#     board[num] = positions[num]
#     board[num] = positions[num]
#     board[num] = positions[num]


# print(board)

# matrix = [[1, 2], [3,4], [5,6], [7,8]]
# transpose = [[row for row in matrix] for i in range(3)]
# print (transpose)

# matrix = [[1, 2], [3,4], [5,6], [7,8]]
# transpose = [[row[i] for row in matrix] for i in range(2)]
# print (transpose)
# mat=[[1,2],[3,4]]
# print(mat[4])

# adad = 0
# for i in range(3):
#     row = []
#     for j in range(3):

#         row.append(positions[i])
#         adad += 1

obj1 = Minimax('X', 'O')
boar = obj1.generate_2d(positions)
print(boar)

# print(mini.generate_2d(positions,3))
# a = obj1.generate_1d(boar)
# a = obj1.findBestMove(boar)
# print(a)


# import time

# for i in range(3):
#     dot = "."
#     for j in range(4):
#         time.sleep(0.2)
#         print(f"Bot is chosing {dot}")
#         dot += "."
        
# print(max(50,50))

