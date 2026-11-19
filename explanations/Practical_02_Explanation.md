# Practical 2: Code Explanation & Viva Guide
## 🗺️ Route Planning using BFS and DFS

---

### 🎯 Aim of the Practical
To implement and compare **Breadth-First Search (BFS)** and **Depth-First Search (DFS)** algorithms for pathfinding and route planning on an unweighted network graph.

---

### 🧩 Chunk-by-Chunk Code Breakdown

#### 🔹 Chunk 1: Graph Representation
```python
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
```
- **What it does:**
  - Imports `deque` (double-ended queue) from Python's standard `collections` module.
  - Represents the map / network as an **Adjacency List** using a Python dictionary where each key is a city/node and its value is a list of connected neighboring nodes.
- **Viva Examiner Tip:**
  - *Examiner:* "Why use an Adjacency List instead of an Adjacency Matrix?"
  - *Answer:* An Adjacency List uses $\mathcal{O}(V + E)$ memory, which is much more space-efficient for sparse graphs than an Adjacency Matrix ($\mathcal{O}(V^2)$).

---

#### 🔹 Chunk 2: Breadth-First Search (BFS)
```python
def bfs(start, goal):
    queue = deque([[start]])
    visited = {start}
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None
```
- **What it does:**
  - Uses `queue = deque([[start]])` to store paths in a First-In-First-Out (**FIFO**) order.
  - `visited = {start}` tracks visited nodes using a Python `set` for $\mathcal{O}(1)$ lookup.
  - While nodes remain in the queue:
    1. Pops the oldest path: `path = queue.popleft()`.
    2. Inspects the last node of the path: `node = path[-1]`.
    3. If `node == goal`, immediately returns the path.
    4. Otherwise, iterates through unvisited neighbors, marks them visited, and appends the extended path `path + [neighbor]` to the back of the queue.
- **Viva Examiner Tip:**
  - *Examiner:* "Why `queue.popleft()` instead of `list.pop(0)`?"
  - *Answer:* `list.pop(0)` takes $\mathcal{O}(N)$ time because all elements must shift left. `deque.popleft()` takes $\mathcal{O}(1)$ constant time.
  - *Examiner:* "Why does BFS guarantee the shortest path here?"
  - *Answer:* Because it explores all paths of length 1, then all paths of length 2, etc. The first time the goal is reached, it is guaranteed to have the minimum number of edges.

---

#### 🔹 Chunk 3: Depth-First Search (DFS)
```python
def dfs(start, goal):
    stack = [[start]]
    visited = set()
    while stack:
        path = stack.pop()
        node = path[-1]
        if node not in visited:
            visited.add(node)
            if node == goal:
                return path
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(path + [neighbor])
    return None
```
- **What it does:**
  - Uses `stack = [[start]]` as a Last-In-First-Out (**LIFO**) structure using a standard Python list.
  - `stack.pop()` pops the most recently added path, exploring as deep as possible along each branch before backtracking.
  - `reversed(...)` is used so that neighbors are pushed in reverse order, allowing the first adjacent neighbor to be processed first when popped.

---

#### 🔹 Chunk 4: Driver Execution
```python
if __name__ == "__main__":
    print("BFS Shortest Path (A to F):", bfs('A', 'F'))
    print("DFS Path          (A to F):", dfs('A', 'F'))
```
- **Output:**
  - BFS Result: `['A', 'C', 'F']` (Length = 2 hops)
  - DFS Result: `['A', 'B', 'E', 'F']` (Length = 3 hops)

---

### 🎤 Top Viva Questions & Instant Answers for Practical 2

**Q1: What are the Time and Space Complexities?**
- **Time Complexity:** Both take $\mathcal{O}(V + E)$ where $V$ is vertices and $E$ is edges.
- **Space Complexity:**
  - BFS: $\mathcal{O}(V)$ (needs to store all nodes of the current level).
  - DFS: $\mathcal{O}(d)$ (where $d$ is maximum tree depth).

**Q2: When would you prefer DFS over BFS?**
- When memory is strictly limited, or when the solution is known to be located deep in the tree and there are many alternative shallow branches.

**Q3: Is BFS complete and optimal?**
- Yes, BFS is complete (will always find a solution if one exists) and optimal for unweighted graphs.
