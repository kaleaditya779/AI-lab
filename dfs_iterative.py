from collections import deque

stack = deque()
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

def dfs_iterative(initial_vert):
    stack.append(initial_vert)
    visited.add(initial_vert)

    while stack:
        vert = stack.pop()
        for adjacent in graph[vert]:
            if adjacent not in visited:
                stack.append(adjacent)
                visited.add(adjacent)

def main():
    verti = int(input("Enter the starting vertex: "))
    dfs_iterative(verti)
    print("The nodes/vertices visited using DFS (not in the sequence of visit):", visited)

if __name__ == "__main__":
    main()
