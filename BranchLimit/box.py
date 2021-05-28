def Box(s0,k):
    global m1
    if k == n:
        if s0 > m1:
            m1 = s0
        return
    Box(s0, k + 1) 
    # min0 = 20001
    # for i in range(k, n):
    #     if v1[i] < min0:
    #         min0 = v1[i]
    # # print(min0)
    # if s0 + min0 <= v:
    if s0 + v1[k] <= v:
        Box(s0+v1[k], k+1)
           

if __name__ == '__main__':
    m1 = 0
    v = int(input())
    n = int(input())
    v1 = []
    for i in range(n):
        v1.append(int(input()))
    v1.sort(reverse = True)
    Box(0, 0)
    print(v - m1)