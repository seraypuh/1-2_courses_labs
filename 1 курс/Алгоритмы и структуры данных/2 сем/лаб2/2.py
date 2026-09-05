n, m, k = map(int, input().split())
museum = []
for i in range(3*n):
    weight, cost = map(int, input().split())
    museum.append([weight, cost])
museum.sort(key=lambda x: x[1]/x[0])
museum = list(reversed(museum))
total = 0
for i in range(m):
    count_weight = 0
    count_cost = 0
    for item in museum:
        if count_weight + item[0] <= k:
            count_weight += item[0]
            count_cost += item[1]
            museum.remove(item)
    total += count_cost
print(total)