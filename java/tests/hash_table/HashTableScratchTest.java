package data_structures.hash_table;


import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class HashTableScratchTest {

    @Test
    void putAndGetSingleElement() {
        HashTableScratch<String, Integer> table = new HashTableScratch<>();

        table.put("a", 1);

        assertEquals(1, table.get("a"));
        assertEquals(1, table.size());
        assertTrue(table.contains("a"));
    }

    @Test
    void getNonExistingKeyThrows() {
        HashTableScratch<String, Integer> table = new HashTableScratch<>();

        table.put("a", 1);

        IllegalStateException ex = assertThrows(
                IllegalStateException.class,
                () -> table.get("b")
        );

        assertTrue(ex.getMessage().contains("Key not found"));
    }

    @Test
    void updateExistingKey() {
        HashTableScratch<String, Integer> table = new HashTableScratch<>();

        table.put("a", 1);
        table.put("a", 2); // update

        assertEquals(2, table.get("a"));
        assertEquals(1, table.size());
    }

    @Test
    void removeExistingKey() {
        HashTableScratch<String, Integer> table = new HashTableScratch<>();

        table.put("a", 1);
        table.put("b", 2);

        boolean removed = table.remove("a");

        assertTrue(removed);
        assertEquals(1, table.size());
        assertFalse(table.contains("a"));
        assertTrue(table.contains("b"));

        assertThrows(IllegalStateException.class, () -> table.get("a"));
    }

    @Test
    void removeNonExistingKey() {
        HashTableScratch<String, Integer> table = new HashTableScratch<>();

        table.put("a", 1);

        boolean removed = table.remove("b");

        assertFalse(removed);
        assertEquals(1, table.size());
        assertTrue(table.contains("a"));
    }

    @Test
    void containsKeyBehavior() {
        HashTableScratch<String, Integer> table = new HashTableScratch<>();

        table.put("a", 1);
        table.put("b", 2);

        assertTrue(table.contains("a"));
        assertTrue(table.contains("b"));
        assertFalse(table.contains("c"));
    }

    @Test
    void sizeReflectsNumberOfElements() {
        HashTableScratch<String, Integer> table = new HashTableScratch<>();

        assertEquals(0, table.size());

        table.put("a", 1);
        table.put("b", 2);
        table.put("c", 3);

        assertEquals(3, table.size());

        table.remove("b");

        assertEquals(2, table.size());
    }

    @Test
    void collisionsAreHandledCorrectly() {
        HashTableScratch<BadKey, Integer> table = new HashTableScratch<>(4, 0.75);

        BadKey k1 = new BadKey("k1");
        BadKey k2 = new BadKey("k2");
        BadKey k3 = new BadKey("k3");

        table.put(k1, 10);
        table.put(k2, 20);
        table.put(k3, 30);

        assertEquals(3, table.size());
        assertEquals(10, table.get(k1));
        assertEquals(20, table.get(k2));
        assertEquals(30, table.get(k3));

        // remove in the middle of the chain
        assertTrue(table.remove(k2));
        assertFalse(table.contains(k2));

        assertEquals(10, table.get(k1));
        assertEquals(30, table.get(k3));
    }

    @Test
    void rehashIsTriggeredAndPreservesElements() {
        HashTableScratch<String, Integer> table = new HashTableScratch<>(2, 0.75);

        table.put("a", 1);
        table.put("b", 2);
        table.put("c", 3); // here rehash must happen

        assertEquals(3, table.size());

        assertEquals(1, table.get("a"));
        assertEquals(2, table.get("b"));
        assertEquals(3, table.get("c"));

        assertTrue(table.remove("b"));
        assertEquals(2, table.size());
        assertFalse(table.contains("b"));
    }

    // ----------------------------
    //   Helper to force collision 
    // ----------------------------
    private static class BadKey {
        private final String id;

        BadKey(String id) {
            this.id = id;
        }

        @Override
        public int hashCode() {
            // force all keys falls into the same bucket
            return 42;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (!(obj instanceof BadKey)) return false;
            BadKey other = (BadKey) obj;
            return this.id.equals(other.id);
        }

        @Override
        public String toString() {
            return "BadKey{" + id + '}';
        }
    }
}
