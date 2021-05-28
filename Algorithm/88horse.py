import random
import numpy as np
max_n = 6
l1 = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

def check(x, y, chessboard):
    if x < 0 or x > max_n-1:  # 越界
        return False
    if y < 0 or y > max_n-1:
        return False
    if chessboard[x][y] != 0:  # 已经走过  两个隐性条件
        return False
    return True

def checkend(x0, y0, x, y):
    if abs(x-x0) == 1 and abs(y-y0) == 2:
        return True
    elif abs(x-x0) == 2 and abs(y-y0) == 1:
        return True
    return False

def output(chessboard):
    print(chessboard)
    
def jump(chessboard, x, y, num, x0, y0):

    if num == 64 and checkend(x, y):
        output(chessboard)
        # print(1)
        # exit()  # mean end all the programming
    for i in range(max_n):
        x1 = x + l1[i][0]
        y1 = y + l1[i][1]
        if check(x1, y1, chessboard):
            # t = (x1, y1)
            chessboard[x1][y1] = num+1
            # print(Chessboard)
            # list1.append(t)
            # print('({}, {})'.format(x1, y1), end=' ')
            jump(chessboard, x1, y1, num+1, x0, y0)
            chessboard[x1][y1] = 0
            # list1.pop()
            # chessboard[x1][y1] = 0
            
if __name__ ==  '__main__':
    # print(1)
    Chessboard = np.zeros((max_n, max_n), dtype=int)
    x0 = random.randint(0, max_n-1)
    y0 = random.randint(0, max_n-1)
    Chessboard[x0][y0] = 1
    
    # print('({}, {})'.format(x0, y0), end=' ')            
    jump(Chessboard, x0, y0, 1, x0, y0)
    # print(1)
    # print(chessboard)