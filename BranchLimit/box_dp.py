if __name__ == '__main__':
    v=int(input())
    n=int(input())
    v1=[]
    max1=0
    dp=[0]*20005
    for i in range(n):
        v1.append(int(input()))
    for i in range(n):
        for j in range(v,v1[i]+1,-1):
            dp[j]=max(dp[j], dp[j-v1[i]]+v1[i])
    print(v-dp[v])