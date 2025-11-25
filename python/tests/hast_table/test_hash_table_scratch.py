import pytest
from data_structures.hash_table.hash_table_scratch  import HashTable

def test_put_and_get_single_element():
    ht = HashTable()
    ht.put("a", 1)

    assert ht.get("a") == 1
    assert len(ht) == 1
    assert ht.contains("a") is True


def test_get_raises_keyerror_for_missing_key():
    ht = HashTable()
    ht.put("a", 1)

    with pytest.raises(KeyError):
        ht.get("b")


def test_update_existing_key():
    ht = HashTable()
    ht.put("a", 1)
    ht.put("a", 2)  # update

    assert ht.get("a") == 2
    assert len(ht) == 1


def test_remove_existing_key():
    ht = HashTable()
    ht.put("a", 1)
    ht.put("b", 2)

    removed = ht.remove("a")

    assert removed is True
    assert len(ht) == 1
    assert ht.contains("a") is False
    assert ht.contains("b") is True

    with pytest.raises(KeyError):
        ht.get("a")


def test_remove_non_existing_key():
    ht = HashTable()
    ht.put("a", 1)

    removed = ht.remove("b")
    assert removed is False
    assert len(ht) == 1
    assert ht.contains("a") is True


def test_contains_key():
    ht = HashTable()
    ht.put("a", 1)
    ht.put("b", 2)

    assert ht.contains("a") is True
    assert ht.contains("b") is True
    assert ht.contains("c") is False


def test_len_reflects_number_of_elements():
    ht = HashTable()
    assert len(ht) == 0

    ht.put("a", 1)
    ht.put("b", 2)
    ht.put("c", 3)

    assert len(ht) == 3

    ht.remove("b")
    assert len(ht) == 2


def test_collisions_are_handled_correctly(monkeypatch):
    """Força colisões manipulando a função _hash."""
    ht = HashTable(capacity=4)

    # All keys will have the same hash => same bucket
    def fake_hash(key):
        return 42

    monkeypatch.setattr(ht, "_hash", fake_hash)

    ht.put("a", 1)
    ht.put("b", 2)
    ht.put("c", 3)

    assert len(ht) == 3
    assert ht.get("a") == 1
    assert ht.get("b") == 2
    assert ht.get("c") == 3

    # Remove the middle of chain
    assert ht.remove("b") is True
    assert ht.contains("b") is False
    assert ht.get("a") == 1
    assert ht.get("c") == 3


def test_rehash_is_triggered_and_preserves_elements():
    # small capacity to force quick rehash
    ht = HashTable(capacity=2, load_factor=0.75)

    ht.put("a", 1)
    ht.put("b", 2)
    ht.put("c", 3)  # here probably already was reshash

    assert len(ht) == 3

    # All the elements sill might be available
    assert ht.get("a") == 1
    assert ht.get("b") == 2
    assert ht.get("c") == 3

    # And remove still might workds
    assert ht.remove("b") is True
    assert len(ht) == 2
    assert ht.contains("b") is False
