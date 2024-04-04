# Hash Table

An ADT that provides efficient adding, searching and deletion operations.

Each item stored in a hash table must have a unique key.

## Operations

- add
- search
- delete

With a perfect hash table implementation, these operations are expected to run in constant time, i.e. O(1). However, they can still reach O(n) if the hash table is not constructed well.

## Use Cases

- tracking the number of each item
- data caching

## Hash function

A **hash function** is a function that maps a set of keys $K$ to a set of hash values $H$.

The time complexity of operations in a hash table depends on the implementation of the hash function.

### Collision

A collision occurs when more than one key is mapped to the same hash value.

There exists various techiniques that can be applied to handle collision (collision resolution), for example:

- seperate chaining
- open addressing

### Properties of a Hash Function

Therefore, the hash function must have these properties:

- type dependent -> depends on the type of the item's key
- return value within array's range

The hash function ideally would also have these properties:

- fast
- minimse collisions -> distribute keys by hash values uniformly

A perfect hash function is one that relies on very particular properties of the keys to eliminate the possibility of collision entirely. (This is almost impossible to achieve in real scenarios)

Universal hashing is also a good hashing method in theory, as it applies a family of hash functions $|F|$ such that $|F| = k$. For each key, it picks a random hash function $|F|$. This gurantees the chance of collision to be $\le \frac{1}{table \; size}$

Therefore, a good hash function improves in the direction towards a perfect hash function (i.e. minimises collision).

## Defining Hash Functions

We will define a hash function for a string.

### Naive hash function

We can use the values of the characters to create a hash function.

```python
def hash(word: str) -> int:
    value = 0
    for char in word:
        value += ord(char) # get ASCII value
    return value
```

However, this will result in a lot of collisions, particularly in anagrams (words that have same letters but in different positions).

### Character position

We can take the position of the characters into account to improve the hash function.

```python
def hash(word: str) -> int:
    value = 0
    for n, char in enumerate(word):
        value += ord(char) * (26 ** n) # consider position of character using base 26
    return value
```

This would work, but the resulting spread of hash values is too large, and would not fit our table.

### Horner's method

The solution is to clamp the value back to the size of the hash table in each iteration.

we can also introduce a multiplier to each key, and the resulting polynomial fits the description of Horner's method.

[Horner's method](https://en.wikipedia.org/wiki/Horner%27s_method) is an algorithm for polynomial evaluation based on Horner's rule.

It allows for the evaluation of a polynomial of degree $n$ with only $n$ multiplications and $n$ additions, which is optimal.

Horner's Rule states that polynomials can be expressed as follows:

$$a_0 + a_1x + a_2x^2 + a_3x^3 + \cdots + a_nx^n = a_0 + x(a_1 + x(a_2 + x(a_3 + \cdots + x(a_{n-1} + xa_n) \cdots )))$$

Implementing Horner's method, we will end up with the hash function below:

```python
def hash(word: str) -> int:
    BASE = 31
    TABLE_SIZE = 101
    value = 0
    for char in word:
        value = (value * BASE + ord(char)) % TABLE_SIZE
    return value
```

The function repeatedly adds the next character's ASCII value to the previous value multiplied by base, and then clamps it to TABLE_SIZE.

The values of BASE and TABLE_SIZE are recommended to be prime / coprime as they will reduce collisions in hash values.

Having common factors between BASE and TABLE_SIZE results in keys with close hash values (clustering) or even same value (collision).

TABLE_SIZE should also be relatively large as to minimise collisions.

### Different coefficients for each key position

We can alter the key value every iteration to minimise collisions further.

```python
def hash(word: str) -> int:
    BASE = 31415
    ALT = 27183
    TABLE_SIZE = 101
    value = 0
    for char in word:
        value = (value * BASE + ord(char)) % TABLE_SIZE
        BASE = BASE * ALT % (TABLE_SIZE - 1)
    return value
```

## Collision Resolution

### Seperate Chaining

Seperate chaining is a way to address collisions in a hash table.

Simply put, it appends colliding keys to a linked list or balanced tree which contains all the colliding keys for that hash value.

However, this will make the time complexity of operations become O(n).
