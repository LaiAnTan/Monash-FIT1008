# Recursion

A recursive algorithm is used to solve problems that are recursive in nature.

Problems of recursive nature are:

- problems that can be reduced into one or more sub problems
  - Of the same kind of the original
  - simpler than the original

Such problems should have a base case, i.e. a sub problem which can be solved without further reduction.

## Recursive Notation

a) Unary, binary, n-ary recursion

- Unary -> single recursive call
- Binary -> two recursive calls
- n-ary -> n recursive calls

b) Direct, Indirect recursion

- Direct -> recursive calls are calls to the same function
- Indirect -> recusion through two or more methods

c) Tail, Non - tail recursion

- Tail -> recursive call as the last operation in the function before returning

```python
def factorial(n):

    return aux(n, 1)


def aux(n, 1)

    if n == 0:
        return result
    else:
        return aux(n - 1, result * n)
```

- Non tail -> recursion involves other operations after the recursive call

```python
def factorial(n):

    return n * factorial(n - 1)
```

## Recursion to Iteration

We can convert functions that are recursive in nature into functions that are iterative.

### Accumulators

Accumulators are variables that "accumulate" the result of the function over recursive calls.

This can make it more efficient as less recomputation is required.

For example, consider this naive recursive function to calculate the nth fibonnacci number.

```python
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
```

Now, the function is rewritted with accumulators.

```python
def fib(n):

    return fib_aux(n, 0, 1)


def fib_aux(n, fm1, fm2):
    if n == 0:
        return fm2
    
    return fib_aux(n - 1, fm1, fm2 + fm1)
```


### Stack