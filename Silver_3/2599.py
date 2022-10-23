N = int(input())
am, af = map(int, input().split())
bm, bf = map(int, input().split())
cm, cf = map(int, input().split())
ans = [[0, 0], [0, 0], [0, 0]]
if am <= (N-af) and bm <= (N-bf) and cm <= (N-cf) and am+bm+cm == af+bf+cf:
    print(1)
    print(bf, am-bf)
    print(af-cm, cf+bf-am)
    print(cm, 0)
else:
    print(0)
