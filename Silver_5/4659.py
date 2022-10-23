while True:
    s = input()
    if s == 'end':
        break
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0
    in_vowel = False
    pre_i = ''
    flag = True
    for i in s:
        if i in vowels:
            vowel_count += 1
            consonant_count = 0
            in_vowel = True
            if vowel_count >= 3:
                flag = False
            if pre_i == i:
                if i == 'e' or i == 'o':
                    continue
                else:
                    flag = False
        else:
            vowel_count = 0
            consonant_count += 1
            if consonant_count >= 3:
                flag = False
            if pre_i == i:
                flag = False
        pre_i = i
    if in_vowel and flag:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')
