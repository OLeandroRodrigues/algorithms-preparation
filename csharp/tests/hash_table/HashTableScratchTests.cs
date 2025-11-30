using System;
using System.Collections.Generic;
using DataStructures.HashTable;
using Xunit;

namespace DataStructures.HashTable;

public class HashTableScratchTests
{
    [Fact]
    public void Put_And_Get_Single_Element()
    {
        var table = new HashTableScratch<string, int>();

        table.Put("a", 1);

        Assert.Equal(1, table.Get("a"));
        Assert.True(table.Contains("a"));
        Assert.Equal(1, table.Size());
    }

    [Fact]
    public void Get_Missing_Key_Should_Throw()
    {
        var table = new HashTableScratch<string, int>();
        table.Put("a", 1);

        Assert.Throws<KeyNotFoundException>(() => table.Get("b"));
    }

    [Fact]
    public void Put_Should_Update_Existing_Key()
    {
        var table = new HashTableScratch<string, int>();

        table.Put("a", 1);
        table.Put("a", 2); // update

        Assert.Equal(2, table.Get("a"));
        Assert.Equal(1, table.Size());
    }

    [Fact]
    public void Remove_Existing_Key_Should_Return_True_And_Decrease_Size()
    {
        var table = new HashTableScratch<string, int>();

        table.Put("a", 1);
        table.Put("b", 2);

        var removed = table.Remove("a");

        Assert.True(removed);
        Assert.False(table.Contains("a"));
        Assert.True(table.Contains("b"));
        Assert.Equal(1, table.Size());
        Assert.Throws<KeyNotFoundException>(() => table.Get("a"));
    }

    [Fact]
    public void Remove_Non_Existing_Key_Should_Return_False()
    {
        var table = new HashTableScratch<string, int>();

        table.Put("a", 1);

        var removed = table.Remove("b");

        Assert.False(removed);
        Assert.True(table.Contains("a"));
        Assert.Equal(1, table.Size());
    }

    [Fact]
    public void Contains_Should_Work_For_Existing_And_NonExisting_Keys()
    {
        var table = new HashTableScratch<string, int>();

        table.Put("a", 1);
        table.Put("b", 2);

        Assert.True(table.Contains("a"));
        Assert.True(table.Contains("b"));
        Assert.False(table.Contains("c"));
    }

    [Fact]
    public void Size_Should_Reflect_Number_Of_Elements()
    {
        var table = new HashTableScratch<string, int>();

        Assert.Equal(0, table.Size());

        table.Put("a", 1);
        table.Put("b", 2);
        table.Put("c", 3);

        Assert.Equal(3, table.Size());

        table.Remove("b");

        Assert.Equal(2, table.Size());
    }

    // Auxiliar to force colisions 
    private sealed class BadHashKey
    {
        public int Id { get; }

        public BadHashKey(int id)
        {
            Id = id;
        }

        public override int GetHashCode()
        {
            // all at the same bucket
            return 42;
        }

        public override bool Equals(object obj)
        {
            return obj is BadHashKey other && other.Id == Id;
        }

        public override string ToString() => $"BadHashKey({Id})";
    }

    [Fact]
    public void Collisions_Should_Be_Handled_With_Chaining()
    {
        var table = new HashTableScratch<BadHashKey, string>();

        var k1 = new BadHashKey(1);
        var k2 = new BadHashKey(2);
        var k3 = new BadHashKey(3);

        table.Put(k1, "one");
        table.Put(k2, "two");
        table.Put(k3, "three");

        Assert.Equal(3, table.Size());
        Assert.Equal("one", table.Get(k1));
        Assert.Equal("two", table.Get(k2));
        Assert.Equal("three", table.Get(k3));

        
        var removed = table.Remove(k2);
        Assert.True(removed);

        Assert.False(table.Contains(k2));
        Assert.True(table.Contains(k1));
        Assert.True(table.Contains(k3));
        Assert.Equal(2, table.Size());
    }

    [Fact]
    public void Rehash_Should_Preserve_All_Elements()
    {
        
        var table = new HashTableScratch<string, int>(capacity: 2, loadFactor: 0.75);

        table.Put("a", 1);
        table.Put("b", 2);
        table.Put("c", 3);
        table.Put("d", 4);

        Assert.Equal(4, table.Size());
        Assert.Equal(1, table.Get("a"));
        Assert.Equal(2, table.Get("b"));
        Assert.Equal(3, table.Get("c"));
        Assert.Equal(4, table.Get("d"));

        
        Assert.True(table.Remove("b"));
        Assert.False(table.Contains("b"));
        Assert.Equal(3, table.Size());
    }

    [Fact]
    public void CurrentLoadFactor_Should_Be_Consistent_With_Size_And_Capacity()
    {
        var table = new HashTableScratch<string, int>(capacity: 4, loadFactor: 0.75);

        Assert.Equal(0, table.Size());
        Assert.Equal(0.0, table.CurrentLoadFactor(), 5);

        table.Put("a", 1);
        table.Put("b", 2);

        var expectedLoadFactor = (double)table.Size() / 4.0;
        Assert.Equal(expectedLoadFactor, table.CurrentLoadFactor(), 5);
    }

    [Fact]
    public void ToString_Should_Not_Throw_And_Contain_Pairs()
    {
        var table = new HashTableScratch<string, int>();

        table.Put("a", 1);
        table.Put("b", 2);

        var text = table.ToString();

        Assert.False(string.IsNullOrWhiteSpace(text));
        Assert.Contains("a", text);
        Assert.Contains("1", text);
        Assert.Contains("b", text);
        Assert.Contains("2", text);
    }
}

