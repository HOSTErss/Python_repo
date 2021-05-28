import numpy as np

def tri(A, B):
    n = A.shape[0]  # 获取方程组的行数和列数
    u = np.zeros((n, n))  # 上三角
    l = np.zeros((n, n))  # 下三角
    y = np.zeros((n, 1))
    x = np.zeros((n, 1))
    # 第一行和第一列
    for i in range(0, n):
        u[0][i] = A[0][i]
        l[i][0] = A[i][0]/u[0][0]
    
    # 上三角和下三角的其他行和其他列
    for k in range(1, n):
        for j in range(k, n):
            s1 = 0
            for r in range(0, k):
                s1 += l[k][r]*u[r][j]
            u[k][j] = A[k][j] - s1
        for i in range(k, n):
            s2 = 0
            for r in range(0, k):
                s2 += l[i][r]*u[r][k]
            l[i][k] = (A[i][k] - s2) / u[k][k]

    # 回带求y
    for k in range(0, n):
        s1 = 0 
        for j in range(0, k):
            s1 += l[k][j]*y[j]
        y[k] = B[k] - s1
    
    # 回代求x
    for k in range(n-1, -1, -1):
        s2 = 0
        for j in range(k+1, n):
            s2 += u[k][j]*x[j]
        x[k] = (y[k] - s2)/u[k][k]
    return (l,u,y,x)
            

if __name__ == "__main__":
    A = np.array([[12,-3,3],[-18,3,-1],[1,1,1]])
    B = np.array([15,-15,6])
    # A = np.array([[1,1,1],[0,2,5],[2,5,-1]])
    # B = np.array([6,-4,27])
    (l, u, y, x) = tri(A,B)
    
    np.set_printoptions(precision = 3)
    print("l = \n{}".format(l))
    print("u = \n{}".format(u))
    print("y = \n{}".format(y))
    print("x = \n{}".format(x))
