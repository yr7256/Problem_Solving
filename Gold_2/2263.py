import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
position = [0]*(N+1)
for i in range(N):
    position[inorder[i]] = i


def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    root = postorder[post_end]
    print(root, end=' ')
    left = position[root]-in_start
    right = in_end-position[root]
    preorder(in_start, in_start+left-1, post_start, post_start+left-1)
    preorder(in_end-right+1, in_end, post_end-right, post_end-1)


preorder(0, N-1, 0, N-1)
