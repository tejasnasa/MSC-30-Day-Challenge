n = int(input())

coun = []

for i in range(n):
    x = input()
    coun.append(x)

print(len(set(coun)))
