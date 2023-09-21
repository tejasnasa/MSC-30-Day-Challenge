def print_formatted(number):
  a = len(str(bin(number))) - 2
  i = 1
  while (i < number + 1):
    print(str(i).rjust(a," "), str(oct(i))[2:].rjust(a," "), str(hex(i))[2:].rjust(a," ").upper(), str(bin(i))[2:].rjust(a," "))
    i += 1
  return

if __name__ == '__main__':
  n = int(input())
  print_formatted(n)
