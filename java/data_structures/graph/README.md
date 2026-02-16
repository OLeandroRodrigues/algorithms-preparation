# 📝 Graph & Digraph Proof

## 📚 Metadata

-   **Creator / Inventor:** Foundations in graph theory (Euler and later
    formalization)
-   **Country of Origin:** Switzerland / Germany (early graph theory in
    Europe)
-   **Institution (if applicable):** Early mathematical literature;
    later adopted in computer science
-   **Year of Creation / Publication:** 1736 (Euler's Königsberg
    bridges); modern formalization in 20th century
-   **Primary Reference:** *Introduction to Algorithms* --- Cormen,
    Leiserson, Rivest, Stein (CLRS)
-   **Related Concepts:** Vertex (Node), Edge (Arc), Adjacency, Degree,
    Path, Walk, Cycle, Connected Components, DAG
-   **Typical Use Cases:** Networks, routing, dependencies, scheduling,
    state machines, knowledge graphs, social graphs

------------------------------------------------------------------------

## 📝 Description

A **Graph** is a data structure that models relationships between
entities.

Formally:

-   **Undirected Graph** G = (V, E) where V is a set of vertices and E
    is a set of unordered pairs {u,v}.

-   **Directed Graph (Digraph)** G = (V, A) where A is a set of ordered
    pairs (u,v) called arcs.

### Core Operations (typical)

-   `add_vertex(v)`
-   `add_edge(u, v)` or `add_arc(u, v)`
-   `neighbors(u)`
-   `has_edge(u, v)` / `has_arc(u, v)`
-   iteration over vertices and edges/arcs

------------------------------------------------------------------------

## 🧱 Representations

Different representations trade time vs memory.

### 1) Adjacency List

Stores for each vertex a list of its neighbors.

Example (undirected):

    A: B, D
    B: A, C
    C: B
    D: A

Good for **sparse graphs**.

### 2) Adjacency Matrix

For a graph with |V| vertices, we define a matrix M of size |V| × |V|.

M[u][v] = 1 if (u,v) ∈ E   (or ∈ A for directed graphs)
M[u][v] = 0 otherwise

For undirected graphs:
M[u][v] = M[v][u]  (matrix is symmetric)

Good for dense graphs and O(1) adjacency check, but uses more memory.

------------------------------------------------------------------------

## 📝 Pseudocode

### 0) Data Model (Adjacency List)

``` text
STRUCT Graph:
    adj : map<Vertex, list<Vertex>>
    directed : boolean

ADD_VERTEX(G, v):
1  if v not in G.adj:
2      G.adj[v] = empty list

ADD_EDGE(G, u, v):
1  ADD_VERTEX(G, u)
2  ADD_VERTEX(G, v)
3  append v to G.adj[u]
4  if G.directed == false:
5      append u to G.adj[v]

NEIGHBORS(G, u):
1  return G.adj[u]
```

### 1) Data Model (Adjacency Matrix)

``` text
STRUCT GraphMatrix:
    vertices : list<Vertex>
    index    : map<Vertex, int>
    M        : matrix<int>   // |V| x |V|
    directed : boolean

ADD_VERTEX(G, v):
1  if v already in index: return
2  add v to vertices
3  index[v] = |vertices|-1
4  expand M with new row and column filled with 0

ADD_EDGE(G, u, v):
1  ADD_VERTEX(G, u)
2  ADD_VERTEX(G, v)
3  i = index[u], j = index[v]
4  M[i][j] = 1
5  if directed == false:
6      M[j][i] = 1

HAS_EDGE(G, u, v):
1  if u or v not in index: return false
2  return M[index[u]][index[v]] == 1
```

------------------------------------------------------------------------

## 1. Invariant

At any moment, the structure preserves:

### For Adjacency List

- Every vertex in the graph appears as a key in `adj`.
- For every edge/arc recorded, endpoints exist in `adj`.
- For undirected graphs, adjacency is symmetric:

  v in adj[u]  if and only if  u in adj[v]

### For Adjacency Matrix

- M is always square and matches the number of vertices.
- The index mapping is consistent with the vertex list.
- For undirected graphs, the matrix is symmetric:

  M[i][j] = M[j][i]

------------------------------------------------------------------------

## 2. Correctness

### Add Vertex

Ensures the vertex exists in the graph and can be referenced safely by
all other operations.

### Add Edge / Add Arc

-   Ensures both endpoints exist (via ADD_VERTEX).
-   Updates representation so that future NEIGHBORS / HAS_EDGE queries
    reflect the new relationship.
-   If undirected, guarantees symmetry is preserved.

### Neighbors / Has Edge

Returns exactly the edges/arcs stored in the representation.

Thus, all updates preserve the invariants and all queries reflect the
current structure.

------------------------------------------------------------------------

## 3. Termination

-   All operations iterate over finite collections:
    -   adjacency lists are finite
    -   matrix updates are constant-time assignments
-   Therefore all methods terminate.

------------------------------------------------------------------------

## 4. Time Complexity

Let \|V\| = number of vertices, \|E\| = number of edges.

### Adjacency List

-   Add vertex: O(1) average
-   Add edge: O(1) amortized
-   Neighbors(u): O(deg(u))
-   Has edge(u,v): O(deg(u))

### Adjacency Matrix

-   Add vertex: O(\|V\|\^2)
-   Add edge: O(1)
-   Has edge: O(1)
-   Neighbors(u): O(\|V\|)

------------------------------------------------------------------------

## 5. Space Complexity

### Adjacency List

O(\|V\| + \|E\|)

### Adjacency Matrix

O(\|V\|\^2)

------------------------------------------------------------------------

## 6. Additional Notes

-   Use Adjacency List for sparse graphs.
-   Use Adjacency Matrix for dense graphs or constant-time adjacency
    checks.
-   For faster has_edge with adjacency list, store neighbors as a set
    instead of a list.

------------------------------------------------------------------------

## 7. Handwritten Draft (optional)

(Insert your notes here.)
