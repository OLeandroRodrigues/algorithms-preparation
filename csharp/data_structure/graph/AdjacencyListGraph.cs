using System;
using System.Collections.Generic;

namespace DataStructures.Graph;

public sealed class AdjacencyListGraph<T> : AbstractGraph<T>
    where T : notnull
{
    private readonly Dictionary<T, List<T>> _adjList = new();
    private readonly Dictionary<T, HashSet<T>> _adjSet = new();

    public AdjacencyListGraph(bool directed = false) : base(directed) { }

    // -----------------------------
    // AbstractGraph implementation
    // -----------------------------
    public override void AddVertex(T v)
    {
        // T : notnull already prevents null for reference types,
        // but this keeps the error message explicit.
        if (v is null)
            throw new ArgumentException("AddVertex: vertex cannot be null", nameof(v));

        if (_adjList.ContainsKey(v))
            return;

        _adjList[v] = new List<T>();
        _adjSet[v] = new HashSet<T>();
    }

    public override void AddEdge(T u, T v)
    {
        if (u is null || v is null)
            throw new ArgumentException("AddEdge: u and v cannot be null");

        AddVertex(u);
        AddVertex(v);

        AddArc(u, v);

        if (!Directed)
            AddArc(v, u);
    }

    public override IEnumerable<T> Neighbors(T v)
    {
        if (!_adjList.TryGetValue(v, out var nbrs))
            throw new KeyNotFoundException($"Neighbors: vertex '{v}' not found in graph");

        // return the list directly (stable insertion order)
        return nbrs;
    }

    public override bool HasEdge(T u, T v)
    {
        return _adjSet.TryGetValue(u, out var set) && set.Contains(v);
    }

    public override IEnumerable<T> Vertices()
    {
        return _adjList.Keys;
    }

    // -----------------------------
    // Helpful extras (optional)
    // -----------------------------
    public IEnumerable<(T U, T V)> Edges()
    {
        if (Directed)
        {
            foreach (var (u, nbrs) in _adjList)
                foreach (var v in nbrs)
                    yield return (u, v);

            yield break;
        }

        // Undirected: return each edge once
        var seen = new HashSet<(T, T)>();

        foreach (var (u, nbrs) in _adjList)
        {
            foreach (var v in nbrs)
            {
                var key = CanonicalEdge(u, v);
                if (seen.Add(key))
                    yield return key;
            }
        }
    }

    public override string ToString()
    {
        var kind = Directed ? "Directed" : "Undirected";
        return $"{kind}AdjacencyListGraph(|V|={_adjList.Count})";
    }

    // -----------------------------
    // Internal helpers
    // -----------------------------
    private void AddArc(T u, T v)
    {
        // u and v already exist
        var set = _adjSet[u];
        if (set.Contains(v))
            return;

        set.Add(v);
        _adjList[u].Add(v);
    }

    private static (T, T) CanonicalEdge(T a, T b)
    {
        // We avoid requiring T : IComparable<T>.
        // Canonicalize using hash + tie-breaker by string representation.
        int ha = a.GetHashCode();
        int hb = b.GetHashCode();

        if (ha < hb) return (a, b);
        if (ha > hb) return (b, a);

        var sa = a.ToString() ?? "";
        var sb = b.ToString() ?? "";
        return string.CompareOrdinal(sa, sb) <= 0 ? (a, b) : (b, a);
    }
}

