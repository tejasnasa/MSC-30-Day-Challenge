if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
seclowsco = sorted(list(set([x[1] for x in students])))[1]

res = []
for i in range (0, len(students)):
    if (students[i][1] == seclowsco):
        res.append(students[i][0])

print("\n".join(sorted(res)))
