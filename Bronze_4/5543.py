ham = []
dri = []
for i in range(3):
    i = int(input())
    ham.append(i)
for i in range(2):
    i = int(input())
    dri.append(i)
print(min(ham)+min(dri)-50)
