package data_structures.graph;

import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;
import java.util.NoSuchElementException;
import java.util.Set;
import java.util.HashSet;

import static org.junit.jupiter.api.Assertions.*;

class AdjacencyListGraphTest {

    private static <T> List<T> toList(Iterable<T> it) {
        List<T> out = new ArrayList<>();
        for (T x : it) out.add(x);
        return out;
    }

    @Test
    void addVertex_initializesEmptyNeighbors() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(false);
        g.addVertex("A");

        assertTrue(g.containsVertex("A"));
        assertEquals(List.of(), toList(g.neighbors("A")));
    }

    @Test
    void addVertex_isIdempotent() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(false);
        g.addVertex("A");
        g.addVertex("A");

        assertEquals(1, g.size());
        assertEquals(List.of(), toList(g.neighbors("A")));
    }

    @Test
    void addVertex_rejectsNull() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(false);
        assertThrows(IllegalArgumentException.class, () -> g.addVertex(null));
    }

    @Test
    void addEdge_createsVerticesIfMissing_undirected() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(false);
        g.addEdge("A", "B");

        assertTrue(g.containsVertex("A"));
        assertTrue(g.containsVertex("B"));
        assertTrue(g.hasEdge("A", "B"));
        assertTrue(g.hasEdge("B", "A"));

        assertEquals(List.of("B"), toList(g.neighbors("A")));
        assertEquals(List.of("A"), toList(g.neighbors("B")));
    }

    @Test
    void addEdge_createsVerticesIfMissing_directed() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(true);
        g.addEdge("A", "B");

        assertTrue(g.hasEdge("A", "B"));
        assertFalse(g.hasEdge("B", "A"));

        assertEquals(List.of("B"), toList(g.neighbors("A")));
        assertEquals(List.of(), toList(g.neighbors("B")));
    }

    @Test
    void addEdge_rejectsNullEndpoints() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(false);

        assertThrows(IllegalArgumentException.class, () -> g.addEdge(null, "B"));
        assertThrows(IllegalArgumentException.class, () -> g.addEdge("A", null));
    }

    @Test
    void addEdge_avoidsDuplicates_undirected() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(false);
        g.addEdge("A", "B");
        g.addEdge("A", "B"); // duplicate
        g.addEdge("B", "A"); // same edge other direction

        assertEquals(List.of("B"), toList(g.neighbors("A")));
        assertEquals(List.of("A"), toList(g.neighbors("B")));
    }

    @Test
    void addEdge_avoidsDuplicates_directed() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(true);
        g.addEdge("A", "B");
        g.addEdge("A", "B"); // duplicate

        assertEquals(List.of("B"), toList(g.neighbors("A")));
        assertEquals(List.of(), toList(g.neighbors("B")));
    }

    @Test
    void neighbors_preservesInsertionOrder() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(true);
        g.addEdge("A", "B");
        g.addEdge("A", "C");
        g.addEdge("A", "D");

        assertEquals(List.of("B", "C", "D"), toList(g.neighbors("A")));
    }

    @Test
    void neighbors_unknownVertex_throws() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(false);
        assertThrows(NoSuchElementException.class, () -> toList(g.neighbors("X")));
    }

    @Test
    void vertices_returnsAllVertices() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(false);
        g.addEdge("A", "B");
        g.addVertex("C");

        List<String> vs = toList(g.vertices());
        assertEquals(Set.of("A", "B", "C"), new HashSet<>(vs));
    }

    @Test
    void size_containsVertex_isEmpty_work() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(false);

        assertTrue(g.isEmpty());
        assertEquals(0, g.size());

        g.addEdge("A", "B");

        assertFalse(g.isEmpty());
        assertEquals(2, g.size());
        assertTrue(g.containsVertex("A"));
        assertTrue(g.containsVertex("B"));
        assertFalse(g.containsVertex("C"));
    }

    @Test
    void degree_undirected() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(false);
        g.addEdge("A", "B");
        g.addEdge("A", "C");

        assertEquals(2, g.degree("A"));
        assertEquals(1, g.degree("B"));
        assertEquals(1, g.degree("C"));
    }

    @Test
    void degree_directed_isOutDegree() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(true);
        g.addEdge("A", "B");
        g.addEdge("A", "C");
        g.addEdge("B", "C");

        assertEquals(2, g.degree("A")); // out-degree
        assertEquals(1, g.degree("B"));
        assertEquals(0, g.degree("C"));
    }

    @Test
    void edges_directed_returnsAllArcs() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(true);
        g.addEdge("A", "B");
        g.addEdge("A", "C");
        g.addEdge("B", "C");

        List<AdjacencyListGraph.Edge<String>> es = toList(g.edges());
        assertEquals(3, es.size());

        assertTrue(es.contains(new AdjacencyListGraph.Edge<>("A", "B")));
        assertTrue(es.contains(new AdjacencyListGraph.Edge<>("A", "C")));
        assertTrue(es.contains(new AdjacencyListGraph.Edge<>("B", "C")));
    }

    @Test
    void edges_undirected_returnsEachEdgeOnce() {
        AdjacencyListGraph<String> g = new AdjacencyListGraph<>(false);
        g.addEdge("A", "B");
        g.addEdge("B", "C");
        g.addEdge("A", "C");

        List<AdjacencyListGraph.Edge<String>> es = toList(g.edges());
        assertEquals(3, es.size());

        // canonicalization might return (A,B) or (B,A), so test as an undirected set:
        Set<Set<String>> undirectedEdges = new HashSet<>();
        for (AdjacencyListGraph.Edge<String> e : es) {
            undirectedEdges.add(Set.of(e.u, e.v));
        }

        assertTrue(undirectedEdges.contains(Set.of("A", "B")));
        assertTrue(undirectedEdges.contains(Set.of("B", "C")));
        assertTrue(undirectedEdges.contains(Set.of("A", "C")));
    }
}
