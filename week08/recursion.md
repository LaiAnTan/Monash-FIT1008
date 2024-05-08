# Recursion

A recursive algorithm is used to solve problems that are recursive in nature.

Problems of recursive nature are:

- problems that can be reduced into one or more sub problems
  - Of the same kind of the original
  - simpler than the original

Such problems should have a base case, i.e. a sub problem which can be solved without further reduction.

## General Recursive Structure

A recursive function must have:

- at least 1 base case
- at least 1 recursive calls
- convergence of recursive calls to base case
- combining the subsolutions to solve problems

## Recursion Tree

A recursion tree can be used to map out the recursive calls of a function.

## Examples of Recursion

### Factorial

```python
def factorial(n):

    if n == 0: # base case
        return 1
    
    return n * factorial(n - 1) # recursive case + combine subsolution

```

The recursion tree of factorial is as follows:

```md
f(n) -> f(n - 1) -> f(n - 2) -> ... -> f(1) -> f(0) (base case)
```

### Fibonacci

```python
def fibonacci(n):

    # two base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # convergence of recursive calls and combination of subsolutions
    return fibonacci(n - 1) + fibonacci(n - 2)

```

The recursion tree of fibonacci(5) is as follows:
![alt text](/assets/fib_recursion_tree.png)

## Recursion and Iteration

Every iterative function can be implemented with recursion:

- iterations are replaced with recursive function calls
- base case is the condition of the loop

Every recursive function can be implemented using iteration:

- using accumulators / stack

## Pros / Cons of Recursion

Recursion Pros:

- more intuitive / natural
- easier to prove correct
- easier to analyse

Recursion Cons:

- run time overhead
- memory intensive (memory overhead)

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

The function above does multiple computations of the same values, as evident in the recursion tree [above](#fibonacci).

Now, the function is rewritted with accumulators.

```python
def fib(n):

    return fib_aux(n, 0, 1)


def fib_aux(n, fm2, fm1):
    if n == 0:
        return fm2
    
    return fib_aux(n - 1, fm1, fm2 + fm1)
```

This version of fibonacci using accumulators to store previously calculated values is more efficient compared to naive recursion.

However it is not very clear how the function works compared to the naive version.

Now, we can easily transform the recursive function that uses accumulators to use an iterative approach.

```python
def fib(n):

    fm1 = 0
    fm2 = 1

    while n > 0:
        n  -= 1
        fm1, fm2 = fm2, fm1 + fm2

    return fm2
```

#### Naive Recursion vs Recursion w/ Accumulators

Naive recursion:

- clear
- valuable as a description of mathematical properties
- bad solving algorithm

Recursion w/ accumulators

- less clear
- more efficient
- easily converted to iterative version

### Preamble: Inner workings of Recursion

The system implements recursion using a runtime stack.

Each recursive call reserves a new stack area (stack frame).

After a recursive call finishes the stack frame is popped, and control returns to the calling function (previous stack frame).

If the recursion is too deep and the call stack is too large, a stack overflow error occurs.

### Stack

A stack can be used to keep track of the order of recursive calls.

Consider the following recursive function to find the power of $x$ to $n$, $x^n$.

```python
def power(x, n):

    temp = 1

    if n > 0:
        temp = power(x, n / 2)
        if n % 2 == 0:
            temp = temp * temp
        else:
            temp = temp * temp * x
        
    return temp
```

We can transfor this to an iterative method as follows:

```python
def power(x, n):
    stack = Stack()

    # stack to keep track of all values of n that we need to calculate, as n converges to 0
    while n > 0:
        stack.push(n)
        n = n // 2
    
    # calculate power
    temp = 1
    while not stack.is_empty()
        if stack.pop() % 2 == 0:
            temp = temp * temp
        else:
            temp = temp * temp * x
    
    return temp
```
