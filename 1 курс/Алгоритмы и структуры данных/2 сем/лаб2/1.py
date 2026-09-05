n = int(input())
m1, s1 = map(int, input().split())
m2, s2 = map(int, input().split())
m3, s3 = map(int, input().split())
m4, s4 = map(int, input().split())
coins = [[m1, s1], [m2, s2], [m3, s3], [m4, s4]]
coins.sort(key=lambda x: x[1])
coins = list(reversed(coins))
res = []
for i in range(4):
    while n >= coins[i][1] and coins[i][0] != 0:
        n -= coins[i][1]
        coins[i][0] -= 1
        res.append(coins[i][1])
    if n <= coins[-1][1] and n != 0:
        n += res[-1]
        res.pop()
if n != 0: print("размен невозможен")
else: print(res)