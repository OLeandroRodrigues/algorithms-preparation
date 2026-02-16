using System;
using System.Collections.Generic;

namespace DataStructures.Graph
{
    public abstract class AbstractGraph<T>
        where T : notnull
    {
        protected AbstractGraph(bool directed = false)
        {
            Directed = directed;
        }

        public bool Directed { get; }

        // ---------------------------------
        // Abstract API (must be implemented)
        // ---------------------------------

        public abstract void AddVertex(T v);

        public abstract void AddEdge(T u, T v);

        public abstract IEnumerable<T> Neighbors(T v);

        public abstract bool HasEdge(T u, T v);

        public abstract IEnumerable<T> Vertices();

        // ---------------------------------
        // Concrete shared behavior
        // ---------------------------------

        public bool ContainsVertex(T v)
        {
            foreach (var x in Vertices())
            {
                if (EqualityComparer<T>.Default.Equals(x, v))
                    return true;
            }
            return false;
        }

        public int Size()
        {
            int count = 0;
            foreach (var _ in Vertices()) count++;
            return count;
        }

        /// <summary>
        /// Degree of v. For directed graphs, this is the out-degree.
        /// </summary>
        public int Degree(T v)
        {
            int count = 0;
            foreach (var _ in Neighbors(v)) count++;
            return count;
        }

        public bool IsEmpty() => Size() == 0;
    }
}
