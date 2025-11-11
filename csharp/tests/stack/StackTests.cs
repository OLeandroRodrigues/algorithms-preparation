
using DataStructure.Stack;
using Xunit;
using System;

namespace DataStructure.Tests.Stack;

public class StackTests
{
    [Fact]
    public void Push_And_Peek_Should_Work_Correctly()
    {
        var stack = new DataStructure.Stack.Stack<int>();
        Assert.True(stack.IsEmpty());

        stack.Push(10);
        stack.Push(20);
        stack.Push(30);

        Assert.False(stack.IsEmpty());
        Assert.Equal(3, stack.Size());
        Assert.Equal(30, stack.Peek());

        Console.WriteLine("Push_And_Peek_Should_Work_Correctly passed successfully!");
    }

    [Fact]
    public void Pop_Should_Follow_Lifo_Order()
    {
        
        var stack = new DataStructure.Stack.Stack<string>();
        stack.Push("A");
        stack.Push("B");
        stack.Push("C");

        Assert.Equal("C", stack.Pop());
        Assert.Equal("B", stack.Pop());
        Assert.Equal("A", stack.Pop());
        Assert.True(stack.IsEmpty());

        Console.WriteLine("Pop_Should_Follow_Lifo_Order passed successfully!");
    }

    [Fact]
    public void Peek_Should_Not_Remove_The_Element()
    {
        var stack = new DataStructure.Stack.Stack<int>();
        stack.Push(42);

        int top = stack.Peek();
        Assert.Equal(42, top);
        Assert.False(stack.IsEmpty());
        Assert.Equal(1, stack.Size());

        Console.WriteLine("Peek_Should_Not_Remove_The_Element passed successfully!");
    }

    [Fact]
    public void Pop_On_Empty_Should_Throw_Exception()
    {
        var stack = new DataStructure.Stack.Stack<int>();
        Assert.Throws<InvalidOperationException>(() => stack.Pop());

        Console.WriteLine("Pop_On_Empty_Should_Throw_Exception passed successfully!");
    }

    [Fact]
    public void Peek_On_Empty_Should_Throw_Exception()
    {
        var stack = new DataStructure.Stack.Stack<string>();
        Assert.Throws<InvalidOperationException>(() => stack.Peek());

        Console.WriteLine("Peek_On_Empty_Should_Throw_Exception passed successfully!");
    }

    [Fact]
    public void ToString_Should_Return_Readable_Representation()
    {
        var stack = new DataStructure.Stack.Stack<int>();
        stack.Push(1);
        stack.Push(2);

        string repr = stack.ToString();
        Assert.Contains("Stack", repr);
        Assert.Contains("elements", repr);

        Console.WriteLine("ToString_Should_Return_Readable_Representation passed successfully!");
    }
}

