# data_structures/graph/base.py

from abc import ABC, abstractmethod
from typing import Iterable, Hashable


class AbstractGraph(ABC):
    """
    Base abstraction for Graph structures.

    Defines the minimal contract that all graph implementations
    (adjacency list, adjacency matrix, directed, undirected)
    must satisfy.
    """

    def __init__(self, directed: bool = False):
        self._directed = directed

    # ---------------------------------
    # Properties
    # ---------------------------------
    @property
    def directed(self) -> bool:
        """Return whether the graph is directed."""
        return self._directed

    # ---------------------------------
    # Abstract API (must be implemented)
    # ---------------------------------

    @abstractmethod
    def add_vertex(self, v: Hashable) -> None:
        """Add a vertex to the graph."""
        raise NotImplementedError

    @abstractmethod
    def add_edge(self, u: Hashable, v: Hashable) -> None:
        """Add an edge (or arc if directed) between u and v."""
        raise NotImplementedError

    @abstractmethod
    def neighbors(self, v: Hashable) -> Iterable[Hashable]:
        """Return all neighbors of vertex v."""
        raise NotImplementedError

    @abstractmethod
    def has_edge(self, u: Hashable, v: Hashable) -> bool:
        """Return True if an edge/arc from u to v exists."""
        raise NotImplementedError

    @abstractmethod
    def vertices(self) -> Iterable[Hashable]:
        """Return all vertices in the graph."""
        raise NotImplementedError

    # ---------------------------------
    # Concrete shared behavior
    # ---------------------------------

    def __contains__(self, v: Hashable) -> bool:
        """Allow 'v in graph' syntax."""
        return v in self.vertices()

    def __len__(self) -> int:
        """Number of vertices."""
        return sum(1 for _ in self.vertices())

    def degree(self, v: Hashable) -> int:
        """
        Return the degree of vertex v.

        For directed graphs, this returns the out-degree.
        """
        return sum(1 for _ in self.neighbors(v))

    def is_empty(self) -> bool:
        """Return True if the graph has no vertices."""
        return len(self) == 0
