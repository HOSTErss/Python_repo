def cal(s, l):
    # print(l, end='  ')
    sum = 1
    tmp = 0
    length = len(l)
    for i in range(length):
        if l[i] == 1:    
            e1 = int(s[tmp:i+1])
            sum *= e1
            tmp = i+1
    e1 = int(s[tmp:])
    sum *= e1
    # print(sum)
    return sum


# 关键变量: pos, loc, l(三者都是动态更新的,其中l尤为重要,通过回溯,其值不断改变)   存储变量:  最终结果res, 
def mul_rec(k, s, pos, loc, ins, l, res):  # pos: depth  mean when to stop
    if pos == k+1:
        ans = cal(s, l)
        res.append(ans)
    else:
        for i in range(loc, ins):
            l[i] = 1
            mul_rec(k, s, pos+1, i+1, ins, l, res)
            l[i] = 0    

def mul(n, k, s):
    ins = n-1
    l = [0]*ins
    max_n = 0
    res = []  # 将计算结果存入到列表中, 而不是返回出来
    for i in range(ins):
        l[i] = 1
        mul_rec(k, s, 2, i+1, ins, l, res)
        l[i] = 0
        # print(ans)
        # max_n = max(max_n, ans)
    max_n = max(res)
    return max_n


if __name__ == '__main__':
    # n = int(input())
    # k = int(input())
    list1 = map(lambda x:int(x), input().split())
    n = next(list1)
    k = next(list1)
    s = input()
    max_n = mul(n, k, s)
    print(max_n)
    