def inorder(n):
    global num
    if n <= len(tree)-1:
        inorder(n*2)
        tree[num][0] = n
        num += 1
        inorder(n*2+1)


N = int(input())
tree = [[0, 0]] + [[0, i] for i in list(map(int, input().split()))]
num = 1
inorder(1)
tree.sort()
ans = [i[1] for i in tree[1:]]
print(ans)
num = 1
temp = 1
while temp <= len(tree)-1:
    print(*ans[temp-num:temp])
    num *= 2
    temp += num