using System;
using System.Collections.Generic;
using System.Linq;
using DataStructures.Graph;
using Xunit;

namespace DataStructures.Graph;

public class AdjacencyListGraphTests
{
    [Fact]
    public void AddVertex_Should_Initialize_Empty_Neighbors()
    {
        var g = new AdjacencyListGraph<string>(directed: false);

        g.AddVertex("A");

        Assert.True(g.ContainsVertex("A"));
        Assert.Empty(g.Neighbors("A"));
        Assert.Equal(1, g.Size());
        Assert.False(g.IsEmpty());
    }

    [Fact]
    public void AddVertex_Should_Be_Idempotent()
    {
        var g = new AdjacencyListGraph<string>(directed: false);

        g.AddVertex("A");
        g.AddVertex("A");

        Assert.Equal(1, g.Size());
        Assert.Empty(g.Neighbors("A"));
    }

    [Fact]
    public void AddVertex_Null_Should_Throw()
    {
        var g = new AdjacencyListGraph<string>(directed: false);

        Assert.Throws<ArgumentException>(() => g.AddVertex(null!));
    }

    [Fact]
    public void AddEdge_Should_Create_Vertices_If_Missing_Undirected()
    {
        var g = new AdjacencyListGraph<string>(directed: false);

        g.AddEdge("A", "B");

        Assert.True(g.ContainsVertex("A"));
        Assert.True(g.ContainsVertex("B"));

        Assert.True(g.HasEdge("A", "B"));
        Assert.True(g.HasEdge("B", "A"));

        Assert.Equal(new[] { "B" }, g.Neighbors("A").ToArray());
        Assert.Equal(new[] { "A" }, g.Neighbors("B").ToArray());
    }

    [Fact]
    public void AddEdge_Should_Create_Vertices_If_Missing_Directed()
    {
        var g = new AdjacencyListGraph<string>(directed: true);

        g.AddEdge("A", "B");

        Assert.True(g.HasEdge("A", "B"));
        Assert.False(g.HasEdge("B", "A"));

        Assert.Equal(new[] { "B" }, g.Neighbors("A").ToArray());
        Assert.Empty(g.Neighbors("B"));
    }

    [Fact]
    public void AddEdge_Null_Endpoints_Should_Throw()
    {
        var g = new AdjacencyListGraph<string>(directed: false);

        Assert.Throws<ArgumentException>(() => g.AddEdge(null!, "B"));
        Assert.Throws<ArgumentException>(() => g.AddEdge("A", null!));
    }

    [Fact]
    public void AddEdge_Should_Avoid_Duplicates_Undirected()
    {
        var g = new AdjacencyListGraph<string>(directed: false);

        g.AddEdge("A", "B");
        g.AddEdge("A", "B"); // duplicate
        g.AddEdge("B", "A"); // same edge other direction

        Assert.Equal(new[] { "B" }, g.Neighbors("A").ToArray());
        Assert.Equal(new[] { "A" }, g.Neighbors("B").ToArray());
    }

    [Fact]
    public void AddEdge_Should_Avoid_Duplicates_Directed()
    {
        var g = new AdjacencyListGraph<string>(directed: true);

        g.AddEdge("A", "B");
        g.AddEdge("A", "B"); // duplicate

        Assert.Equal(new[] { "B" }, g.Neighbors("A").ToArray());
        Assert.Empty(g.Neighbors("B"));
    }

    [Fact]
    public void Neighbors_Should_Preserve_Insertion_Order()
    {
        var g = new AdjacencyListGraph<string>(directed: true);

        g.AddEdge("A", "B");
        g.AddEdge("A", "C");
        g.AddEdge("A", "D");

        Assert.Equal(new[] { "B", "C", "D" }, g.Neighbors("A").ToArray());
    }

    [Fact]
    public void Neighbors_Unknown_Vertex_Should_Throw()
    {
        var g = new AdjacencyListGraph<string>(directed: false);

        Assert.Throws<KeyNotFoundException>(() => g.Neighbors("X").ToArray());
    }

    [Fact]
    public void Vertices_Should_Return_All_Vertices()
    {
        var g = new AdjacencyListGraph<string>(directed: false);

        g.AddEdge("A", "B");
        g.AddVertex("C");

        var vs = g.Vertices().ToHashSet();

        Assert.Equal(3, vs.Count);
        Assert.Contains("A", vs);
        Assert.Contains("B", vs);
        Assert.Contains("C", vs);
    }

    [Fact]
    public void Size_ContainsVertex_IsEmpty_Should_Work()
    {
        var g = new AdjacencyListGraph<string>(directed: false);

        Assert.True(g.IsEmpty());
        Assert.Equal(0, g.Size());

        g.AddEdge("A", "B");

        Assert.False(g.IsEmpty());
        Assert.Equal(2, g.Size());
        Assert.True(g.ContainsVertex("A"));
        Assert.True(g.ContainsVertex("B"));
        Assert.False(g.ContainsVertex("C"));
    }

    [Fact]
    public void Degree_Undirected_Should_Work()
    {
        var g = new AdjacencyListGraph<string>(directed: false);

        g.AddEdge("A", "B");
        g.AddEdge("A", "C");

        Assert.Equal(2, g.Degree("A"));
        Assert.Equal(1, g.Degree("B"));
        Assert.Equal(1, g.Degree("C"));
    }

    [Fact]
    public void Degree_Directed_Should_Be_OutDegree()
    {
        var g = new AdjacencyListGraph<string>(directed: true);

        g.AddEdge("A", "B");
        g.AddEdge("A", "C");
        g.AddEdge("B", "C");

        Assert.Equal(2, g.Degree("A"));
        Assert.Equal(1, g.Degree("B"));
        Assert.Equal(0, g.Degree("C"));
    }

    [Fact]
    public void Edges_Directed_Should_Return_All_Arcs()
    {
        var g = new AdjacencyListGraph<string>(directed: true);

        g.AddEdge("A", "B");
        g.AddEdge("A", "C");
        g.AddEdge("B", "C");

        var edges = g.Edges().ToList();

        Assert.Equal(3, edges.Count);
        Assert.Contains(("A", "B"), edges);
        Assert.Contains(("A", "C"), edges);
        Assert.Contains(("B", "C"), edges);
    }

    [Fact]
    public void Edges_Undirected_Should_Return_Each_Edge_Once()
    {
        var g = new AdjacencyListGraph<string>(directed: false);

        g.AddEdge("A", "B");
        g.AddEdge("B", "C");
        g.AddEdge("A", "C");

        var edges = g.Edges().ToList();
        Assert.Equal(3, edges.Count);

        // Treat as undirected: compare by set of endpoints
        var undirected = edges
            .Select(e => new HashSet<string> { e.U, e.V })
            .ToList();

        Assert.Contains(undirected, s => s.SetEquals(new[] { "A", "B" }));
        Assert.Contains(undirected, s => s.SetEquals(new[] { "B", "C" }));
        Assert.Contains(undirected, s => s.SetEquals(new[] { "A", "C" }));
    }

    [Fact]
    public void ToString_Should_Not_Throw_And_Contain_Info()
    {
        var g = new AdjacencyListGraph<string>(directed: false);

        g.AddEdge("A", "B");
        g.AddEdge("A", "C");

        var text = g.ToString();

        Assert.False(string.IsNullOrWhiteSpace(text));
        Assert.Contains("AdjacencyListGraph", text);
        Assert.Contains("|V|=3", text);
    }
}
