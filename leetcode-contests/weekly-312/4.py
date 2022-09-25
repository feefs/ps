# 2421. Number of Good Paths
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        """
        group nodes by value, iterate from lower value groups to higher value groups
          for each group, add nodes to graph and union find
              for each component, find the # of nodes that have current value
          count paths between them, add to result
              nodes with the same value in different components can't form a good path with each other
                  this is because we're adding edges with lower value nodes first!
        """

        N = len(vals)

        # Union Find
        parent = [n for n in range(N)]
        size = [1] * N

        def root(node):
            if parent[node] == node:
                return node
            else:
                return root(parent[node])

        def union(a, b):
            p1, p2 = root(a), root(b)
            if p1 == p2:
                return
            # choose one parent
            if size[p1] < size[p2]:
                p1, p2 = p2, p1
            parent[p2] = p1
            size[p1] += size[p2]

        # adjacency list
        graph = [[] for _ in range(N)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # groups
        groups = defaultdict(lambda: [])
        for i, v in enumerate(vals):
            groups[v].append(i)

        # algo
        result = 0
        added_to_graph = [False] * N
        for value, nodes in sorted(groups.items()):
            for n in nodes:
                added_to_graph[n] = True
                for child in graph[n]:
                    if added_to_graph[child]:
                        union(n, child)

            # count how many nodes with current value are in each component
            components = defaultdict(lambda: 0)
            for n in nodes:
                components[root(n)] += 1
            for V in components.values():
                # for V nodes, the # of paths between two nodes is (V - 1) + ... 1
                # sum formula for 1 + 2 + ... V - 1
                # add V since each node counts as a valid path to itself
                result += ((V * (V - 1)) // 2) + V

        return result
