class Solution:
    def cloneGraph(self,node):
        visited = {}
        def clone(node,visited):
            if node not in visited:
                new_node = UndirectedGraphNode(node)
                visited[node] = new_node
                new_node.neighbors = [clone(n,visited) for n in node.neighbors]
            return visited[node]
        clone(node,visited)
        return visted[node]