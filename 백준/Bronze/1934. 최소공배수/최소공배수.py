#1934 최소공배수

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

check = int(input())

for _ in range(check):
    a, b = map(int, input().split())
    print(lcm(a, b))