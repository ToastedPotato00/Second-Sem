def allPaths(graph, target):
    out = []
    def bt(node, path):
        if node == target:
            return out.append(path[:])
        for nxt in graph.get(node, []):
            path.append(nxt)
            bt(nxt, path)
            path.pop()
    bt(0, [0])
    return out

graph = {0:[1,2], 1:[3], 2:[3], 3:[]}
print(allPaths(graph, 3))
