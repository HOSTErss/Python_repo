import numpy as np


def main_list(A, B):
    n = A.shape[0]
    x = [0]*n  # A的行数和列数
    for k in range(0, n):  # k: each row
        ki = k
        for i in range(k+1, n):  # from k row to n-1 row, find the max in k column
            if A[i][k] > A[ki][k]:
                ki = i
        if k != ki:
            A[[k,ki]] = A[[ki,k]]  # 交换k和ki行
            tmp = B[k]
            B[k] = B[ki]
            B[ki] = tmp
        # check zero in main place and swap if necessary
        found = True
        if A[k][k] == 0:  # make sure the first letter is not zero
            found = False  # first letter is capital
            for s in range(k+1, n):
                if A[s][k] != 0:
                    found = True
                    A[[k,s]] = A[[s,k]]  # change row
                    tmp = B[k]
                    B[k] = B[s]
                    B[s] = tmp
        if not found:  # all ele in k column is zero
            continue

        tmp = A[k][k]
        for i in range(k, n):  # search per column
            A[k][i] /= tmp  
        B[k] /= tmp
        for i in range(k+1, n):   # row
            lik = A[i][k]/A[k][k] # use kth row to kill i row  (top target)
            for j in range(k, n): # column
                A[i][j] -= lik*A[k][j]
            B[i] -= lik*B[k]

        for i in range(n-1, -1, -1):  # 回代
            si = 0
            for t in range(i+1,n):
                si += A[i][t]*x[t]
            d = B[i] - si
            x[i] = d/A[i][i]
    return x


if __name__ == "__main__":
    A = np.array([[12., -3, 3],[-18, 3, -1], [1, 1, 1]])  # attention here decimal point 
    B = np.array([15., -15, 6])
    # A = np.array([[1., 1, 1],[1, -1, 1], [2, 1, 1]])  # attention here decimal point 
    # B = np.array([3., 1, 4])
    x = main_list(A, B)
    n = A.shape[0]
    for i in range(1, n+1):  # 输出结果
        print("x{} = ".format(i), end=" ")
        print("{0:.4f}".format(x[i-1]))