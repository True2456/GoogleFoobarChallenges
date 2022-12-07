def multi(a, b):
    diff = a - b
    return (diff / b) + 1


def solution(x, y):
    step, m, f = 0, int(x), int(y)
    while True:
        if m <= 0 or f <= 0:
            break
        if m > 100 or f > 100:
            if m > f:
                mul = multi(m, f)
                m -= f *