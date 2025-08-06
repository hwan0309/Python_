import sys
input = sys.stdin.read
def ex():
    data = (input().split())
    n, m = int(data[0]), int(data[1])
    que = sorted([int(x) for i in data[2:]] )
    abc = int('int')
    start=0

    for end in range(n):
        while que[end] - que[start] >=m:
            abc = min(abc, que[end] - que[start])
            start += 1

    print(abc)

ex()
