keyboard = ["***ABCDE", "FGHIJKLM", "NOPQRSTU", "VWXYZ***"]
destination = []

N = int(input())
for _ in range(N):
    destination.append(input())

input_string = input()

possible = []
# Find words that start with 'input_string' and collect the next character
for word in destination:
    if word.startswith(input_string):
        possible.append(word[len(input_string)])

# Iterate through the keyboard and print characters accordingly
for row in keyboard:
    for char in row:
        if char in possible:
            print(char, end='')
        else:
            print('*', end='')
    print()