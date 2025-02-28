"""
For the DFS algorithms, a visited set must be declared before the function
For any algorithm using an adjacency list, the adjacency list must be created before calling the function (this is called adj_list in the code)
"""

#DFS for adj list
def dfs(node):
    if node in visited: return 0
    visited.add(node)

    ans = 1
    for next in adj_list[node]:
        ans+=dfs(next)

    return ans

#DFS for grid
def dfs(r, c):
    if (r,c) in visited: return 0
    visited.add((r, c))

    dir = [(-1,0),(1,0),(0,1),(0,-1)]
    ans = 1
    for dr, dc in dir:
        nr, nc = r+dr, c+dc
        if not (0<=nr<N and 0<=nc<N): continue
        ans+=dfs(nr,nc)

    return ans

#BFS for adj list
def bfs(node):
    visited = set()
    queue = []

    queue.append(node)
    ans = 0
    while queue:
        n = queue.pop(0)
        visited.add(n)
        ans+=1

        for next in adj_list[n]:
            if next not in visited:
                queue.append(next)

#BFS for grid
def bfs(r, c):
    visited = set()
    queue = []
    dir = [(-1,0),(1,0),(0,1),(0,-1)]

    queue.append((r,c))
    ans = 0
    while queue:
        rc, cc = queue.pop(0)
        visited.add((rc,cc))
        ans+=1

        for dr, dc in dir:
            nr, nc = rc+dr, cc+dc
            if not (0<=nr<N and 0<=nc<N): continue
            if (nr, nc) in visited: continue
            queue.append((nr,nc))
    return ans
