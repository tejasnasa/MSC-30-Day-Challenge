n = input()
ar = input().split()
A = set(input().split())
B = set(input().split())

count = 0

for i in ar:
    if i in A:
        count += 1
    if i in B:
        count -= 1

print(count)
