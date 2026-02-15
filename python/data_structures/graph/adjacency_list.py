# data_structures/graph/adjacency_list.py
from __future__ import annotations
from typing import Dict, Hashable, Iterable, List, Set, Tuple
from .base import AbstractGraph


class AdjacencyListGraph(AbstractGraph):
    """
    Graph representation using adjacency lists.

    Public behavior:
      - neighbors(v) returns neighbors in insertion order
      - add_edge avoids duplicates
      - supports directed and undirected graphs

    Internal detail:
      - we keep both a list (stable iteration order) and a set (fast membership check)
    """

    def __init__(self, directed: bool = False):
        super().__init__(directed=directed)
        self._adj_list: Dict[Hashable, List[Hashable]] = {}
        self._adj_set: Dict[Hashable, Set[Hashable]] = {}

    # -----------------------------
    # AbstractGraph implementation
    # -----------------------------
    def add_vertex(self, v: Hashable) -> None:
        if v is None:
            raise ValueError("add_vertex: vertex cannot be None")

        if v not in self._adj_list:
            self._adj_list[v] = []
            self._adj_set[v] = set()

    def add_edge(self, u: Hashable, v: Hashable) -> None:
        if u is None or v is None:
            raise ValueError("add_edge: u and v cannot be None")

        self.add_vertex(u)
        self.add_vertex(v)

        self._add_arc(u, v)

        if not self.directed:
            self._add_arc(v, u)

    def neighbors(self, v: Hashable) -> Iterable[Hashable]:
        if v not in self._adj_list:
            raise KeyError(f"neighbors: vertex {v!r} not found in graph")
        return self._adj_list[v]

    def has_edge(self, u: Hashable, v: Hashable) -> bool:
        if u not in self._adj_set:
            return False
        return v in self._adj_set[u]

    def vertices(self) -> Iterable[Hashable]:
        return self._adj_list.keys()

    # -----------------------------
    # Helpful extras (optional)
    # -----------------------------
    def edges(self) -> Iterable[Tuple[Hashable, Hashable]]:
        """
        Iterate over edges/arcs.

        - Directed: yields all arcs (u, v).
        - Undirected: yields each edge once.
        """
        if self.directed:
            for u, nbrs in self._adj_list.items():
                for v in nbrs:
                    yield (u, v)
        else:
            seen = set()
            for u, nbrs in self._adj_list.items():
                for v in nbrs:
                    # canonical representation to avoid duplicates
                    key = (u, v) if (repr(u), repr(v)) <= (repr(v), repr(u)) else (v, u)
                    if key in seen:
                        continue
                    seen.add(key)
                    yield key

    def __repr__(self) -> str:
        kind = "Directed" if self.directed else "Undirected"
        return f"{kind}AdjacencyListGraph(|V|={len(self._adj_list)})"

    # -----------------------------
    # Internal helpers
    # -----------------------------
    def _add_arc(self, u: Hashable, v: Hashable) -> None:
        """
        Add u -> v if not already present.
        Keeps list order stable and membership check fast.
        """
        if v in self._adj_set[u]:
            return
        self._adj_set[u].add(v)
        self._adj_list[u].append(v)
