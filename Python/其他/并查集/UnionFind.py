def find(x):
    global father
    if x == father[x]:
        return father[x]
    else:
        father[x] = find(father[x])
        return father[x]

def union(x, y):
    global father
    a = find(x)
    b = find(y)
    father[b] = a

def make_set(n):
    global father
    for i in range(0, n + 1):
        father.append(i)

father = []
a = list(map(int, input().strip().split()))
n, m, p = a[0], a[1], a[2]
make_set(n)
for i in range(m):
    b = list(map(int, input().strip().split()))
    union(b[0], b[1])

for i in range(p):
    c = list(map(int, input().strip().split()))
    x = find(c[0])
    y = find(c[1])
    if x == y:
        print("true")
    else:
        print("false")
