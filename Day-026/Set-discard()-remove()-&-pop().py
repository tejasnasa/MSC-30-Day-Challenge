n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    com = input()
    if (com[0:3] == "pop"):
        s.pop()
      
    elif (com[0:6] == "remove"):
        s.remove(int(com[7]))
      
    elif (com[0:7] == "discard"):
        s.discard(int(com[8]))

print(sum(s))
