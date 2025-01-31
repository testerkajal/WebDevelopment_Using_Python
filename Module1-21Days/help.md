# Python Concepts: Functions, Methods, and Documentation

## 1. Difference Between Function and Methods

- **Function**:
  - A block of reusable code that performs a specific task.
  - Defined using the `def` keyword.
  - Can be called independently.
  - Example: `len()`, `sum()`, `print()`.

- **Method**:
  - A function that is associated with an object or a class.
  - Called on an object using dot notation (`object.method()`).
  - Acts on the data of the object it belongs to.
  - Example: `str.upper()`, `list.append()`, `dict.keys()`.

---

## 2. How to Find the Methods of a Particular Object

To find the methods available for a specific object (like `str`, `list`, `tuple`, `dictionary`), use the `dir()` function.

### Example:
```python
# List all methods of the `str` object
print(dir(str))

# List all methods of the `list` object
print(dir(list))

# List all methods of the `tuple` object
print(dir(tuple))

# List all methods of the `dict` object
print(dir(dict))
```
## 3. How to Find Information About Any Method
To get detailed information about a specific method (e.g., what it does, its parameters, and return value), use the help() function.

```python
# Example:
# Get help on the `append` method of the `list` object
help(list.append)

# Get help on the `upper` method of the `str` object
help(str.upper)

# Get help on the `keys` method of the `dict` object
help(dict.keys)
```
The help() function provides a description of the method, its syntax, and examples (if available).

