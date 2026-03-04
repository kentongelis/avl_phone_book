# AVL Phone Book

A self-balancing binary search tree (AVL tree) implementation for storing and retrieving phone book entries. Keys are contact names (strings) and values are phone numbers.

## Features

- **O(log n)** insert, lookup, and delete — guaranteed by AVL self-balancing
- Automatic rotations keep the tree height-balanced after every operation
- In-order traversal prints all contacts in alphabetical order

## Files

| File | Description |
|------|-------------|
| `avl_phone_book.py` | Core AVL tree implementation |
| `test_avl_phone_book.py` | Pytest test suite |

## Usage

```python
from avl_phone_book import AVL_Phone_Book

pb = AVL_Phone_Book()

# Add contacts
pb.add("Alice", "555-0101")
pb.add("Bob",   "555-0102")

# Look up a number
pb.get("Alice")          # → "555-0101"
pb.get("Zara")           # → None

# Check existence
pb.contains("Bob")       # → True

# Update a contact (re-add with same key)
pb.add("Alice", "999-9999")

# Delete a contact
pb.delete("Bob")

# Print all contacts alphabetically
pb.inOrderTraversal()
```

## API Reference

| Method | Description |
|--------|-------------|
| `add(key, value)` | Insert or update a contact |
| `get(key)` | Return the phone number, or `None` if not found |
| `contains(key)` | Return `True` if the key exists |
| `delete(key)` | Remove a contact (no-op if not found) |
| `inOrderTraversal()` | Print all contacts in alphabetical order |

## Running Tests

Requires **pytest**:

```bash
pip install pytest
pytest test_avl_phone_book.py -v
```

## How AVL Balancing Works

After every insert or delete the tree checks the **balance factor** (left height − right height) at each node on the path back to the root. If the factor goes outside `[−1, 1]`, one of four rotations is applied:

| Case | Rotation |
|------|----------|
| Left-Left | Single right rotate |
| Left-Right | Left rotate on child, then right rotate |
| Right-Right | Single left rotate |
| Right-Left | Right rotate on child, then left rotate |

This keeps the tree height at **O(log n)**, ensuring fast operations even as the phone book grows.
