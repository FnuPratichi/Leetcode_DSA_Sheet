n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
z = list(map(int, input().split()))


if sum(x)+sum(y)+sum(z) ==0:
    print("YES")
else:
    print("NO")