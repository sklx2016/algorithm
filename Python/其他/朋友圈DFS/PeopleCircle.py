
def findCircleNum(M):
    visited = [False] * len(M)
    count = 0
    for i in range(len(M)):
        if not visited[i]:
            dfs(M, i, visited)
            count += 1
    return count

def dfs(M, i, visited):
    visited[i] = True
    for j in range(len(M[i])):
        if M[i][j] == 1 and not visited[j]:
            dfs(M, j, visited)


M = [[1,1,0, 0],
     [1,1,0, 1],
     [0,0,1, 0],
     [0, 1, 0, 1]]

print(findCircleNum(M))