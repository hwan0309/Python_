n,k = map(int,input().split())
s = list(map(int,input().split()))

ex_1 = 0
odd = 0
answer = 0
for i in range(n):
    if s[i] % 2 == 1:
        odd +=1

        while odd > k:
            if[ex_1] % 2 == 1:
                odd -= 1
            ex_1 += 1
    answer = max(answer, i - ex_1 + 1 - odd)

print(answer)
