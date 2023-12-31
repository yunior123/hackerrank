from collections import Counter
X = int(input())
sizes = Counter(map(int, input().split()))
N = int(input())
money = 0
for i in range(N):
    size, price = map(int, input().split())
    if sizes[size]:
        money += price
        sizes[size] -= 1
print(money)

