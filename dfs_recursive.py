
"""
Algorithm for DFS:
1) We select any vertex as starting vertex
2) Insert the vertex in the visited array
3) Then we visit its neighbouring vertex (any of the neighbor)
4) During that we will push the previous vertex into stack
5) Then repeat the steps from 2 to 4.
6) When we reach the vertex which is completely explored.
7) Then we pop the recent vertex from the stack.
8) Visit another neighbor of it.
9) Repeat the steps 2 to 8
10) When the stack is empty. Then the DFS process is complete.
11) The visited array contains the sequence of our DFS traversal.
"""

visited = set()

graph = {
    1: [2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4],
    4: [1, 3, 5],
    5: [3, 4, 6, 7],
    6: [],
    7: []
}

def dfs_traversal(vert):
    if vert not in visited:
        print(vert, end=" ")
        visited.add(vert)
        for neighbour in graph[vert]:
            dfs_traversal(neighbour)
    
def main():
    starting_vertex = int(input("Enter the starting vertex: "))
    dfs_traversal(starting_vertex)
    print("\nThe vertices traversed (not in the order traversal happend):", visited)

if __name__ == "__main__":
    main()
