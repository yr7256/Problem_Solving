import sys
sys.setrecursionlimit(10**6)
preorder = []
while True:
    try:
        num = int(input())
        preorder.append(num)
    except:
        break


def postorder(left, right):
    if left > right:
        return
    mid = right+1
    root = preorder[left]
    for i in range(left+1, right+1):
        if root < preorder[i]:
            mid = i
            break
    postorder(left+1, mid-1)
    postorder(mid, right)
    print(root)


postorder(0, len(preorder)-1)
