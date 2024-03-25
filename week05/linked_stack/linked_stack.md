# Linked Stack

Another implementation of the Stack ADT that uses nodes.

```python
| 1 | <- top of the stack (head)
| ↓ |
| 3 |
| ↓ |
| 4 |
| ↓ |
| 2 |
| ↓ |
| 5 | <- bottom of the stack
-----
```

## Pros and Cons

Pros:

- Good to resize
- Needs less space than an array based stack if the array is relatively empty

Cons:

- Needs more space than an array based stack if the array is relatively full because extra space is used for links in nodes

- A little slower (slightly larger constant because of creating nodes)
