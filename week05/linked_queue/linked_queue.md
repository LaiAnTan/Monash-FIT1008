# Linked Queue

Another implementation of the Queue ADT that uses nodes.

```python
                     -----------------
Front of the queue ← 1 ← 3 ← 4 ← 2 ← 5 ← Back of the queue
                     -----------------
```

## Pros and Cons

Pros:

- Good to resize
- Needs less space than an array based queue if the array is relatively empty

Cons:

- Needs more space than an array based queue if the array is relatively full because extra space is used for links in nodes

- A little slower (slightly larger constant because of creating nodes)
