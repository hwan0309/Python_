n,m=map(int,input().split())
def1=list(map(int,input().split()))

count, start, end = 0,0,0
cse=0

while True :
    if cse >= m:
        if cse == m:
            count += 1
        cse -= def1[start]
        start += 1
    elif end == n:
        break
    else:
        cse += def1[end]
        end += 1

print(count)