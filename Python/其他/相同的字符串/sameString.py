
def sameString(array):
    map = {}
    res = []
    for i in range(len(array)):
        map_count = {}
        for j in range(len(array[i])):
            map_count[array[i][j]] = map_count.setdefault(array[i][j], 0) + 1
        map_count = sorted(map_count.items(), key = lambda x : x[0])
        print(map_count)
        map[str(map_count)] = map.setdefault(str(map_count), []) + [array[i]]
    print(map)
    for x in map.values():
        res.append(x)
    return res


print(sameString(["aab", "aba", "ccs", "scs", "ssc"]))



