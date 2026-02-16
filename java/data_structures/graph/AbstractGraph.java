package data_structures.graph;

import java.util.Objects;

/**
 * Base abstraction for Graph structures.
 *
 * Defines the minimal contract that all graph implementations
 * (adjacency list, adjacency matrix, directed, undirected)
 * must satisfy.
 */
public abstract class AbstractGraph<V> {

    private final boolean directed;

    protected AbstractGraph(boolean directed) {
        this.directed = directed;
    }

    public boolean isDirected() {
        return directed;
    }

    // ---------------------------------
    // Abstract API (must be implemented)
    // ---------------------------------

    public abstract void addVertex(V v);

    public abstract void addEdge(V u, V v);

    public abstract Iterable<V> neighbors(V v);

    public abstract boolean hasEdge(V u, V v);

    public abstract Iterable<V> vertices();

    // ---------------------------------
    // Concrete shared behavior
    // ---------------------------------

    public boolean containsVertex(V v) {
        for (V x : vertices()) {
            if (Objects.equals(x, v)) return true;
        }
        return false;
    }

    public int size() {
        int count = 0;
        for (V ignored : vertices()) count++;
        return count;
    }

    /** Degree of v. For directed graphs, this is the out-degree. */
    public int degree(V v) {
        int count = 0;
        for (V ignored : neighbors(v)) count++;
        return count;
    }

    public boolean isEmpty() {
        return size() == 0;
    }
}
