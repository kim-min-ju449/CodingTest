def solution(x):
    answer = 0
    a = x // 10000
    b = x // 1000
    c = x // 100 % 10
    d = x // 10 % 10
    e = x % 10

    return x % (a + b + c + d + e) == 0