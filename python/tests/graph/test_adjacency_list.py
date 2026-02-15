import pytest
from data_structures.graph.adjacency_list import AdjacencyListGraph


def test_add_vertex_initializes_empty_neighbors():
    g = AdjacencyListGraph()
    g.add_vertex("A")

    assert "A" in list(g.vertices())
    assert list(g.neighbors("A")) == []


def test_add_vertex_is_idempotent():
    g = AdjacencyListGraph()
    g.add_vertex("A")
    g.add_vertex("A")  # should not duplicate

    assert len(list(g.vertices())) == 1
    assert list(g.neighbors("A")) == []


def test_add_vertex_rejects_none():
    g = AdjacencyListGraph()
    with pytest.raises(ValueError):
        g.add_vertex(None)


def test_add_edge_creates_vertices_if_missing_undirected():
    g = AdjacencyListGraph(directed=False)
    g.add_edge("A", "B")

    assert "A" in g
    assert "B" in g
    assert g.has_edge("A", "B") is True
    assert g.has_edge("B", "A") is True
    assert list(g.neighbors("A")) == ["B"]
    assert list(g.neighbors("B")) == ["A"]


def test_add_edge_creates_vertices_if_missing_directed():
    g = AdjacencyListGraph(directed=True)
    g.add_edge("A", "B")

    assert g.has_edge("A", "B") is True
    assert g.has_edge("B", "A") is False
    assert list(g.neighbors("A")) == ["B"]
    assert list(g.neighbors("B")) == []


def test_add_edge_rejects_none_endpoints():
    g = AdjacencyListGraph()
    with pytest.raises(ValueError):
        g.add_edge(None, "B")
    with pytest.raises(ValueError):
        g.add_edge("A", None)


def test_add_edge_avoids_duplicates_undirected():
    g = AdjacencyListGraph(directed=False)
    g.add_edge("A", "B")
    g.add_edge("A", "B")  # duplicate
    g.add_edge("B", "A")  # same edge, other direction

    assert list(g.neighbors("A")) == ["B"]
    assert list(g.neighbors("B")) == ["A"]


def test_add_edge_avoids_duplicates_directed():
    g = AdjacencyListGraph(directed=True)
    g.add_edge("A", "B")
    g.add_edge("A", "B")  # duplicate

    assert list(g.neighbors("A")) == ["B"]
    assert list(g.neighbors("B")) == []


def test_neighbors_preserves_insertion_order():
    g = AdjacencyListGraph(directed=True)
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("A", "D")

    assert list(g.neighbors("A")) == ["B", "C", "D"]


def test_neighbors_unknown_vertex_raises_keyerror():
    g = AdjacencyListGraph()
    with pytest.raises(KeyError):
        list(g.neighbors("X"))


def test_vertices_returns_all_vertices():
    g = AdjacencyListGraph()
    g.add_edge("A", "B")
    g.add_vertex("C")

    assert set(g.vertices()) == {"A", "B", "C"}


def test_len_and_contains_from_base():
    g = AdjacencyListGraph()
    assert g.is_empty() is True
    assert len(g) == 0

    g.add_edge("A", "B")
    assert g.is_empty() is False
    assert len(g) == 2
    assert ("A" in g) is True
    assert ("B" in g) is True
    assert ("C" in g) is False


def test_degree_from_base_undirected():
    g = AdjacencyListGraph(directed=False)
    g.add_edge("A", "B")
    g.add_edge("A", "C")

    assert g.degree("A") == 2
    assert g.degree("B") == 1
    assert g.degree("C") == 1


def test_degree_from_base_directed_is_out_degree():
    g = AdjacencyListGraph(directed=True)
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "C")

    assert g.degree("A") == 2  # out-degree
    assert g.degree("B") == 1
    assert g.degree("C") == 0
