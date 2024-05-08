# Recursive Sorts

Recursive sorts use a `divide and conquer` approach to sorting.

## Divide and Conquer

A recursive strategy to solve recursive problems:

1. split the original problem into subproblems
2. solve each subproblem independently
3. combine all subproblems' solutions to form the final solution

In terms of sorting, a divide and conquer approach is:

- splitting a list into smaller and smaller parts until the list is sorted (base case)
- combining the lists back into one

The two most prominent recursive sort algorithms are:

- Merge Sort: simple split, complex combine
- Quick Sort: complex split, simple combine

## Merge Sort

Merge Sort is a sort that recursively splits an array into two halves, and then combines the halves in order to form a sorted array.

The easy part of merge sort is the splitting of lists, while the more difficult part is combining the list back such that they will be sorted.

### Time Complexity of Merge Sort

 Time complexity of Merge Sort: `O((n log n) * comp)` for Best / Worst-case, where n is the number of elements in the array and comp is the time complexity of the comparisons.

This is because we keep performing recursion with halves of a list (// 2), therefore the total recursive depth is (log n), where we do n number of operations at each depth.

### Implementation of Merge Sort

Merge sort implementation(s) [here](/week09/merge_sort.py).

Interesting observations:

- mergesort will be called $2n - 1$ times ($2n - 2$ if the main call does not count)
- merge will be called $n - 1$ times

### Stability of Merge Sort

Merge sort is stable.

## Quick Sort

Quick sort is a sort that partitions the array into two parts using a pivot, and then appends them together with the pivot in the middle.

### Choosing a Pivot

Pivot selection greatly affects the time complexity of quick sort. The closer the pivot is to the median of the array, the better the time complexity.

### Time Complexity of Quick Sort

Time complexity of Quick Sort is as follows:

Best-case: `O((n log n) * comp)` when median is always picked as pivot.
Worst-case: `O(n^2 * comp)` when min / max of array is always picked as pivot.

where n is the number of elements in the array, and comp it the time complexity of the comparisons.

This is because the depth of recursion will be `log n` when the pivot is always the median, as the array will always be split in half.

However, if the minimum or maximum is picked as the pivot for every iteration, the depth of recursion will be `n` as the array will be partitioned in a way such that every element is in its own partition.

### Implementation of Quick Sort

Quick sort implementation(s) [here](/week09/quick_sort.py)

### Partitioning Schemes

There are two partitioning schemes that can be used interchangeabaly in quick sort.

a) Lomuto's partitioning scheme

This pseudocode for Lomuto's partitioning scheme is as follows:

```md
1. swap the pivot with the element at the start of the array
2. initialise a boundary index with the starting index that will act as the boundary between elements lesser than and greater than the pivot
3. for each element, compare it with the pivot.
    3a. if the element is smaller than the pivot, increment the boundary index and swap the current element with the element at position boundary
4. swap the pivot back to the correct place which is at position boundary
```

Lomuto's partitioning scheme ensures that the pivot will always be in the correct position relative to all other elements.

However, this partitioning scheme is less efficient that Hoare's as it requires significantly more swaps than it.

b) Hoare's partitioning scheme

Hoare's partitioning scheme is the original partitioning scheme defined by the creator of quick sort, Tony Hoare.

Hoare's partitioning scheme does three times fewer swaps than Lomuto's partitioning scheme, on average.

The pseudocode for Hoare's partitioning scheme is as follows:

```md
1. define two pointers at the start and end indices respectively
2. Define an infinite loop
    2a. increment the start index, stopping when it is no longer smaller than the pivot
    2b. increment the end index, stopping when it is no longer larger than the pivot
    2c. If the two pointers cross, i.e. (start >= end), return end as the boundary
    2d. else, swap the elements at position start and end
```

Hoare's partitioning scheme does not gurantee that the pivot is at the correct position, it only gurantees that the two arrays that are partitioned are sorted relative to each other (the elements in one array are all smaller than the other array, but the elements in each of the arrays are not sorted).

From wikipeda:
> In this scheme, **the pivot's final location is not necessarily at the index that is returned**, as the pivot and elements equal to the pivot can end up anywhere within the partition after a partition step, and may not be sorted until the base case of a partition with a single element is reached via recursion. Therefore, the next two segments that the main algorithm recurse on are (elements ≤ pivot) and (elements ≥ pivot) as opposed to (start..pivot - 1) and (pivot + 1..end) as in Lomuto's scheme.

Further reading [here](https://stackoverflow.com/questions/7198121/quicksort-and-hoare-partition).

### Advantages of Quick Sort over Merge Sort

Quick Sort does not need to copy the elements back like Merge Sort.
Thus, Quick Sort has a smaller constant than Merge Sort (if a good pivot is chosen).

### Stability of Quick Sort

Quick Sort is an unstable sorting algorithm.
