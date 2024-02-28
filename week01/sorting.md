# Sorting

Sorting Algorithms sorts lists of orderable element types.

Unorderable element types such as objects can also be sorted, but a comparison function has to be defined.

```python
def cmp(a, b): # comparison function
    return a > b
```

The output of a sorting algorithm is the sorted list.

## Invariant

An invariant is a property of an algorithm that does not change during its execution.

## Incrementality

An algorithm is incremental if it does not need to re-compute everything
after a small change.

## Stability of Sorting Algorithms

A sorting algorithm is considered stable if it **maintains the relative positions of elements** before and after sorting.

## Basic Sorting Algorithms

### Bubble Sort

#### Bubble Sort Pseudocode

For a singular iteration,

1. Start at element in position $i = 0$
2. Compare elements in position $i$ and $i + 1$
3. Swap $i + 1$ if $i \gt i + 1$
4. Increment $i$ by 1
5. Repeat 1 to 4 until $i = length(list)$

Repeat until list is sorted or iterated $length(list) - 1$ times.

#### Bubble Sort Optimisations

- Only check for swaps up until a certain point
  - For each iteration of bubble sort, the largest unsorted element is `bubbled` (so thats where the name came from) i.e. the largest unsorted element ends up at the end of the list
  - Therefore, we do not have to check the already sorted elements.

- End the algorithm early
  - There is a way to determine if the whole list is sorted, which is to keep track if $> 1$ swaps have happened in the current iteration.
  - If no swaps have happened in a singular iteration, we can conclude that the list is already sorted.

#### Bubble Sort Implementations

Refer [here](/week01/BubbleSort.py).

#### Bubble Sort Incrementality

The naive Bubble Sort algorithm is not incremental, as there is a significant constant number of iterations required to sort the list after introducing a new element.

In the worst case (the new element is the smallest element), all iterations must be run again for the element to be sorted.

However, the optimised Bubble Sort algorithm is incremental. This is because it has the ability to stop if the whole list is sorted.

Then the question arises whether to append the new element to the front or the back of the list.

- Appending to the back of the list may be faster, but it might require more iterations to achieve the sorted list.
- Appending to the front of the list will take 1 extra iteration (considering the swaps required for the element to be at the start of the list), but we know that the element will be sorted after 1 iteration, for a total of 2 iterations.

Therefore, the condition for optimised Bubble Sort to be incremental is:

- Append the new element to the end of the list

#### Bubble Sort Stability

Bubble sort is stable, however a small change will make it unstable (such as changing $>$ to $\geq$).

### Selection Sort

### Selection Sort Pseudocode

1. Start at element in position $i = 0$
2. Find the minimum element in the sublist ranging from $i + 1$ to $length(list) - 1$
3. Swap the elements
4. Increment $i$ by 1
5. Repeat 1 to 4 until $i = length(list)$

#### Selection Sort Implementation

Refer [here](/week01/SelectionSort.py).

#### Selection Sort Incrementality

Selection sort is not incremental.

#### Selection Sort Stability

Selection sort is unstable, as swaps between non - consecutive elements may occur. (i.e. the relative order of elements may be altered)

### Insertion Sort

#### Insertion Sort Pseudocode

For every iteration,

1. Start at element in position $i = 1$ and store it in a temporary variable
2. Starting from $i - 1$, check if each element before $i$ is larger than the element in position $i$
    - If larger, shift the element 1 position to the right by swapping with the element on the right
3. Drecrement $i$ by 1
4. Repeat 2 and 3 until if condition is not fulfilled
5. `Insert` element in the temporary variable into the space created at $i + 1$

Repeat until list is sorted or iterated $length(list) - 1$ times.

#### Insertion Sort Implementation

Refer [here](/week01/InsertionSort.py).

#### Insertion Sort Incrementality

Insertion sort is incremental under specific conditions.

All conditions below must be fulfilled for Insertion Sort to be incremental:

- Append the new element to the end of the list
- Start at the position of the new element (end of list)

This will allow the list to be sorted again after a single iteration.

#### Insertion Sort Stability

Insertion sort is stable, however a small change will make it unstable (such as changing $>$ to $\geq$).
