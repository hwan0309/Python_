a = int(input())
b = int(input())
c = int(input())

abc = a*b*c
# print (abc)

abc_gg = str(abc)

for i in range(10):
    print(abc_gg.count(str(i)))
