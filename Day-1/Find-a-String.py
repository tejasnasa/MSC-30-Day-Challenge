def count_substring(string, sub_string):
    i = 0
    x = 0
    while (i < len(string)):
        if (string[i:(i + len(sub_string))] == sub_string):
            x+=1       
        i+=1
    return x

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
