
def d(n):
    for i in str(n):
        n += int(i)
    return n


def solution():
    a = set(range(1,5000))
    b = set()
    for i in a:
        b.add(d(i))
    return sum(a-b)


print(solution())