def split_and_join(line):
    i = 0
    result = ("")
    while (i < len(line)):
        if line[i].isalpha() or line[i].isdigit():
            result += line[i]
        if line[i].isspace():
            result += ("-")
        i += 1
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
