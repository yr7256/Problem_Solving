word = input()
word_list = []
for i in range(len(word)-2):
    for j in range(i+1, len(word)-1):
        for k in range(j+1, len(word)):
            word_new = word[:j][::-1]+word[j:k][::-1]+word[k:][::-1]
            word_list.append(word_new)
print(min(word_list))
