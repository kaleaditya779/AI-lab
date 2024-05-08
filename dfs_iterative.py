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

    while stack:
        vert = stack.pop()
        if vert not in visited:
            visited.add(vert)
            print(vert, end=" ") # process the node

            # Push unvisited neighbors onto the stack
            for adjacent in graph[vert]:
                if adjacent not in visited:
                    stack.append(adjacent)


def main():
    verti = int(input("Enter the starting vertex: "))
    dfs_iterative(verti)
    print("\nThe nodes/vertices visited using DFS (not in the sequence of visit):", visited)
    print("If you want to store the sequence in which the vertices are visited, just change the visited to list() and add() to append()")

if __name__ == "__main__":
    main()
