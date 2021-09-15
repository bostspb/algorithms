base = 16
x = int(input())
while x > 0:
    digit = x % base
    print(digit, end='\t')
    x //= base
