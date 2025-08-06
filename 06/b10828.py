n = int(input())

stack = []

for i in range(n):
    cmd = input().strip()
    if cmd.startswith("push"):
        i, x = cmd.split()
        stack.append(int(x))

    elif cmd == "pop":
        print(stack.pop() if stack else -1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        print(0 if stack else 1)
    elif cmd == "top":
        print(stack[-1] if stack else -1) 