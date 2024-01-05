
x = list(map(int, input().split()))
y = list(map(int, input().split()))
import itertools
print(*itertools.product(x,y))