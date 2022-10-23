N, L = map(int, input().split())
loc = list(map(int, input().split()))
loc.sort()
count = 1
start = loc[0]
end = loc[0]+L
for i in loc:
    if i < end:
        continue
    else:
        count += 1
        end = i+L
print(count)
