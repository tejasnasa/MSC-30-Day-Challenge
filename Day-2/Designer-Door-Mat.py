s = input()
a = int((int(s.split(" ")[0]) - 3) / 2)
b = int(s.split(" ")[1]) - 1

i = int(a + 1)
while (i > 0):
    print("---" * i + ".|." * (a + 1 - i) + ".|." + ".|." * (a + 1 - i) + "---" * i)
    i -= 1

print("---" * a + "-WELCOME-" + "---" * a)

i = 1
while (i < a + 2):
    print("---" * i + ".|." * (a + 1 - i) + ".|." + ".|." * (a +1 - i) + "---" * i)
    i += 1
