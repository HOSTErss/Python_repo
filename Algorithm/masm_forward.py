
n=int(input())
l=[]
l2=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    l1=list(map(int,input().split()))
    l.append(l1)
l3=[]
l[1][1]=1
for i in range(n):
    l[i][0] = 1
    l[0][i] = 1
    l[n-1][i] = 1
    l[i][n-1] = 1
def backtrack(x,y,l_ist):
    if x==n-2 and y==n-2:
        l3.append(l_ist)
        return

    if y+1<=n-2 and l[x][y+1]==0:
        l[x][y+1] = 1
        backtrack(x,y+1,l_ist+[(x,y+1)])
        l[x][y+1] = 0
        l_ist.pop()
        
    if x+1<=n-2 and l[x+1][y]==0:
        l[x + 1][y] = 1
        backtrack(x+1,y,l_ist+[(x+1,y)])
        l[x + 1][y] = 0
        l_ist.pop()
    
    if y-1>=0  and l[x][y-1]==0:
        l[x][y-1] == 1
        backtrack(x,y-1,l_ist+[(x,y-1)])
        l[x][y-1] == 0
        l_ist.pop()
        
    if x-1>=0 and l[x-1][y]==0:

        l[x-1][y] = 1
        backtrack(x-1,y,l_ist+[(x-1,y)])
        l[x][y-1] == 0
        l_ist.pop()
    
backtrack(1,1,[(1,1)])
if len(l3)==0:
    print('NO')
else:
    for i in l3[0]:
        print('(%d,%d)'%(i[0],i[1]),end='')