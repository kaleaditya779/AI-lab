
"""
The algorithm for BFS:
1) First we start with a vertex
2) insert that vertex in the visited array and queue.
3) Then we explore that vertex.
4) inserting all the vertices into array and queue while exploration.
5) When exploration completes then we pop that vertex out of queue.
6) Then we select the vertex from queue.
7) repeat the steps 3 to 6
8) after all vertices got explored, the queue should be empty.
9) then we stop the BFS.
10) The squence in the array is our BFS sequence.
"""


from  collections import deque

# creating the data structures required for bfs:
visited = list() # to store the vertex which is visited
que = deque() # to store the vertices in seqence to be visited
graph = {
    1: [2,3,4],
    2:[1,3],
    3:[1,2,4],
    4:[1,3,5],
    5:[3,4,6,7],
    6:[],
    7:[]
}

def bfs_traversal(initial_vertex):
    visited.append(initial_vertex)
    que.append(initial_vertex)

    while (que):
        vertex_to_explore = que.popleft()

        # here we iterate (explore the selected vertex)
        for vert in graph[vertex_to_explore]:
            if vert not in visited:
                visited.append(vert)
                que.append(vert)
    print("The BFS sequence is: ",visited)

def main():

    start_vertex = int(input("Input the vertex to start with: "))
    bfs_traversal(start_vertex)

if __name__ == "__main__":
    main()