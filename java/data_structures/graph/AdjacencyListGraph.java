package data_structures.graph;

import java.util.*;

/**
 * Graph representation using adjacency lists.
 *
 * Public behavior:
 *   - neighbors(v) returns neighbors in insertion order
 *   - addEdge avoids duplicates
 *   - supports directed and undirected graphs
 *
 * Internal detail:
 *   - we keep both a list (stable iteration order) and a set (fast membership check)
 */
public class AdjacencyListGraph<V> extends AbstractGraph<V> {

    private final Map<V, List<V>> adjList = new HashMap<>();
    private final Map<V, Set<V>> adjSet  = new HashMap<>();

    public AdjacencyListGraph(boolean directed) {
        super(directed);
    }

    public AdjacencyListGraph() {
        this(false);
    }

    @Override
    public void addVertex(V v) {
        if (v == null) throw new IllegalArgumentException("addVertex: vertex cannot be null");

        if (!adjList.containsKey(v)) {
            adjList.put(v, new ArrayList<>());
            adjSet.put(v, new HashSet<>());
        }
    }

    @Override
    public void addEdge(V u, V v) {
        if (u == null || v == null) {
            throw new IllegalArgumentException("addEdge: u and v cannot be null");
        }

        addVertex(u);
        addVertex(v);

        addArc(u, v);

        if (!isDirected()) {
            addArc(v, u);
        }
    }

    @Override
    public Iterable<V> neighbors(V v) {
        if (!adjList.containsKey(v)) {
            throw new NoSuchElementException("neighbors: vertex '" + v + "' not found in graph");
        }
        return adjList.get(v);
    }

    @Override
    public boolean hasEdge(V u, V v) {
        Set<V> s = adjSet.get(u);
        if (s == null) return false;
        return s.contains(v);
    }

    @Override
    public Iterable<V> vertices() {
        return adjList.keySet();
    }

    // -----------------------------
    // Helpful extras (optional)
    // -----------------------------

    /** Simple pair type for edges. */
    public static final class Edge<V> {
        public final V u;
        public final V v;

        public Edge(V u, V v) {
            this.u = u;
            this.v = v;
        }

        @Override
        public boolean equals(Object o) {
            if (!(o instanceof Edge<?> other)) return false;
            return Objects.equals(u, other.u) && Objects.equals(v, other.v);
        }

        @Override
        public int hashCode() {
            return Objects.hash(u, v);
        }

        @Override
        public String toString() {
            return "(" + u + ", " + v + ")";
        }
    }

    /**
     * Iterate over edges/arcs.
     *
     * - Directed: returns all arcs (u, v).
     * - Undirected: returns each edge once.
     */
    public Iterable<Edge<V>> edges() {
        if (isDirected()) {
            List<Edge<V>> out = new ArrayList<>();
            for (Map.Entry<V, List<V>> e : adjList.entrySet()) {
                V u = e.getKey();
                for (V v : e.getValue()) {
                    out.add(new Edge<>(u, v));
                }
            }
            return out;
        }

        // undirected: avoid duplicates with canonical key (u,v) vs (v,u)
        Set<Edge<V>> seen = new HashSet<>();
        List<Edge<V>> out = new ArrayList<>();

        for (Map.Entry<V, List<V>> e : adjList.entrySet()) {
            V u = e.getKey();
            for (V v : e.getValue()) {
                Edge<V> key = canonicalEdge(u, v);
                if (seen.add(key)) {
                    out.add(key);
                }
            }
        }
        return out;
    }

    @Override
    public String toString() {
        String kind = isDirected() ? "Directed" : "Undirected";
        return kind + "AdjacencyListGraph(|V|=" + adjList.size() + ")";
    }

    // -----------------------------
    // Internal helpers
    // -----------------------------

    private void addArc(V u, V v) {
        // u and v must already exist (addVertex called)
        Set<V> s = adjSet.get(u);
        if (s.contains(v)) return;

        s.add(v);
        adjList.get(u).add(v);
    }

    private Edge<V> canonicalEdge(V a, V b) {
        // Use hash + tie-breaker via toString for stability (no Comparable requirement).
        int ha = (a == null) ? 0 : a.hashCode();
        int hb = (b == null) ? 0 : b.hashCode();

        if (ha < hb) return new Edge<>(a, b);
        if (ha > hb) return new Edge<>(b, a);

        // tie-breaker if hash collides
        String sa = String.valueOf(a);
        String sb = String.valueOf(b);
        if (sa.compareTo(sb) <= 0) return new Edge<>(a, b);
        return new Edge<>(b, a);
    }
}
