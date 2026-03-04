import pytest
from avl_phone_book import AVL_Phone_Book


@pytest.fixture
def phone_book():
    pb = AVL_Phone_Book()
    pb.add("Alice", "555-0101")
    pb.add("Bob", "555-0102")
    pb.add("Charlie", "555-0103")
    pb.add("Diana", "555-0104")
    pb.add("Eve", "555-0105")
    return pb


# --- Insert / Add ---


def test_add_and_get_single():
    pb = AVL_Phone_Book()
    pb.add("Alice", "555-0101")
    assert pb.get("Alice") == "555-0101"


def test_add_multiple(phone_book):
    assert phone_book.get("Bob") == "555-0102"
    assert phone_book.get("Diana") == "555-0104"


def test_add_duplicate_updates_value():
    pb = AVL_Phone_Book()
    pb.add("Alice", "555-0101")
    pb.add("Alice", "999-9999")
    assert pb.get("Alice") == "999-9999"


def test_add_triggers_balance():
    """Insert in sorted order to force rotations."""
    pb = AVL_Phone_Book()
    for name in ["Anna", "Beth", "Cara", "Dana", "Ella"]:
        pb.add(name, "000-0000")
    assert pb.get("Cara") == "000-0000"


# --- Get ---


def test_get_existing_key(phone_book):
    assert phone_book.get("Charlie") == "555-0103"


def test_get_missing_key(phone_book):
    assert phone_book.get("Zara") is None


def test_get_on_empty_tree():
    pb = AVL_Phone_Book()
    assert pb.get("Alice") is None


# --- Contains ---


def test_contains_existing_key(phone_book):
    assert phone_book.contains("Eve") is True


def test_contains_missing_key(phone_book):
    assert phone_book.contains("Zara") is False


def test_contains_on_empty_tree():
    pb = AVL_Phone_Book()
    assert pb.contains("Alice") is False


# --- Delete / Remove ---


def test_delete_leaf_node(phone_book):
    phone_book.delete("Eve")
    assert phone_book.get("Eve") is None


def test_delete_internal_node(phone_book):
    phone_book.delete("Bob")
    assert phone_book.get("Bob") is None
    assert phone_book.get("Alice") == "555-0101"
    assert phone_book.get("Charlie") == "555-0103"


def test_delete_root():
    pb = AVL_Phone_Book()
    pb.add("Alice", "555-0101")
    pb.delete("Alice")
    assert pb.get("Alice") is None


def test_delete_nonexistent_key(phone_book):
    phone_book.delete("Zara")  # Should not raise
    assert phone_book.get("Alice") == "555-0101"


def test_delete_all_entries():
    pb = AVL_Phone_Book()
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        pb.add(name, "000-0000")
    for name in names:
        pb.delete(name)
    for name in names:
        assert pb.get(name) is None


# --- AVL Balance ---


def test_tree_stays_balanced_after_inserts():
    """Root height should stay small (log n) after many inserts."""
    pb = AVL_Phone_Book()
    names = [f"Contact{i:03}" for i in range(63)]
    for name in names:
        pb.add(name, "000-0000")
    assert pb.root.height <= 7  # log2(63) ≈ 6


def test_tree_stays_balanced_after_deletes(phone_book):
    phone_book.delete("Alice")
    phone_book.delete("Charlie")
    assert phone_book.root is not None
    assert phone_book.root.height <= 4


# --- In-Order Traversal ---


def test_inorder_traversal_prints_sorted(phone_book, capsys):
    phone_book.inOrderTraversal()
    captured = capsys.readouterr()
    lines = captured.out.strip().split("\n")
    keys = [line.split()[0] for line in lines]
    assert keys == sorted(keys)
