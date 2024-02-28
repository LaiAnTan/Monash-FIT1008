# Algorithmic (Computational) Complexity

There exist two types of algorithmic complexity:

- **Time Complexity**: How much time does an algorithm spend solving a particular problem
- **Space Complexity**: How much space does an algorithm spend solving a particular problem

Complexity is measured with respect to the input size, i.e.

## Time Complexity

How much time does an algorithm spend solving a particular problem?

i.e. how well the algorithm performs with large inputs?
i.e. how well does the algorithm scale?

> Given an input of size $n$, we can calculate the value $T(n)$ as the number of steps performed by the algorithm on the input.

However, calculating the exact number of steps is often infeasible, therefore we try to determine the most expensive part of the algorithm, i.e. the part that takes the longest time in general to run.

### Input size, $n$

The size of n depends on the context, i.e the type of input.

- Numeric input: Length of its binary representation, $log_2 (n + 1)$ where $n$ is the number of bits of the input in binary

- Collection (list, array, set, stack): Number of elements in collection

- String: Number of characters

- matrix $n \times m$ : Number of rows $n$ and number of columns $m$

- graph / tree: number of nodes

### Big O Notation

**Big O Notation** is a way to characterise functions according to their growth rates (in this case rate of time taken with respect to input size).

The letter $O$ is used because the growth rate is also known as the order of the function.

#### Mathematical Definition

Assume two functions, $f(n)$ and $g(n)$ defined on $n \in \mathbb{N}$.

$$f(n) = O(g(n))$$ if there are two positive constants $n_0$ and $c$ such that:

For all $n \geq n_0$ ,
$$0 \leq f(n) \leq c \times g(n)$$

> $g(n)$ is referred to the **asymptomatic upper bound** for $f(n)$, i.e. as n approaches $+\infty$ .

i.e. **For all values of n, f(n) grows slower than or at the same rate as g(n)**.

#### Common function growth rates

From shortest to longest,

- $O(1)$ : Constant Time
  - Functions that take a fixed amount of time to run, regardless of input size
  - Arithmetic operations

- $O(log\;n)$ : Logarithmic Time
  - Functions that take a logarithmic amount of time to run
  - Binary Search

- $O(n)$ : Linear Time
  - Functions that have a linear growth rate with respect to the input size
  - Iterating through a list

- $O(n ^ 2)$ : Quadratic Time
  - Functions that have a quadratic growth rate with respect to the input size
  - Nested for loop

- $O(x ^ n)$ : Exponential Time
  - Functions with an exponential growth rate with respect to input size
  - Recursive functions that calls itself $> 1$ time

![image](/assets/common_big_o.png)

#### Other Notations

- Big Omega: $g(n)$ is an asymptotic tight bound for $f(n)$
- Big Theta: $g(n)$ is an asymptotic lower boudn for $f(n)$

#### Determining the big O notation of functions

Since it is hard to select $c$ and $n_0$ , we focus on the single component of the function that grows faster than others, i.e. dominates other componenets.

#### Examples

$f(n) = 4n^2 + 1000n + 100$

Since $4n^2$ dominates other components, the big O notation is $O(n^2)$ (We do not take the constant before $n^2$)

#### Operations with Big O notation

- Sum

    if $f_1(n) = O(g_1(n))$ and $f_2(n) = O(g_2(n))$ ,

    then $$f_1(n) + f_2(n) = O(\textbf{max}(g_1(n), g_2(n)))$$

- Product

    if $f_1(n) = O(g_1(n))$ and $f_2(n) = O(g_2(n))$ ,

    then $$f_1(n) \times f_2(n) = O(g_1(n) \times g_2(n))$$

#### Analyzing Time Complexity of Functions

```python
def func0(input_of_size_n):
    for i in range(n):
    ... # constant time operations
    a = b + 2
    ... # constant time operations
    for j in range(100):
        res += func1(res)
    res -= func2(res)

def func1(something):
    ... # assume O(n)


def func2(something):
    ... # assume O(2 ^ 2)
```

Total Time complexity:
$$O(n) \times (O(1) + O(n) + O(2^n))$$
$$O(n) \times  O(2^n)$$
$$O(n\;2^n)$$
