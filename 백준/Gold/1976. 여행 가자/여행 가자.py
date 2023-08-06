def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[x] = y
    else:
        parent[y] = x


N, M = int(input()), int(input())
parent = [i for i in range(N + 1)]
for i in range(N):
    route = list(map(int, input().split()))
    for j in range(i + 1, N):
        if route[j]:
            union_parent(i + 1, j + 1)

planed_city = list(map(int, input().split()))
pre_city_parent = find_parent(planed_city[0])
for city in planed_city[1:]:
    if pre_city_parent != find_parent(city):
        print('NO')
        exit()
    pre_city_parent = find_parent(city)
print('YES')

