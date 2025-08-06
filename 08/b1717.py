import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int,input().split())
parent = [i for i in range(n + 1)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    x = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for _ in range(m):
    op,aa, bb = map(int,input().split())
    if op == 0:
        union(aa,bb)
    else:
        print("YES" if find(aa) == find(bb) else "NO")