import string

def swap_case(s):
    i = 0
    s1 = ("")
    while (i < len(s)):
        if s[i].isupper():
            s1 += s[i].lower()
        if s[i].islower():
            s1 += s[i].upper()
        if s[i].isspace() or s[i].isdigit():
            s1 += s[i]
        if s[i] in string.punctuation:
            s1 += s[i]
        i += 1
    return s1

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
