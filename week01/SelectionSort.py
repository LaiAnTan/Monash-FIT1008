
def findMinimumIndex(lst, start):

    """
    Helper function to find the index of a minimum of one part of a list,
    starting from start to the end of the list.

    Formula is as follows:
    index of local minimum relative to list slice
    + indices before start of list slice
    = index of local minimum relative to the whole list
    """

    return lst[start:].index(min(lst[start:])) + start


def selectionSort(lst):

    """
    Naive Selection Sort Algorithm.

    Sorts elements by locating the minimum element in a subarray of
    (i + 1 to len(lst) - 1), then swapping the
    positions of the current element (i) with the minimum.

    :param lst: list to be sorted.
    :return lst: the sorted list.
    :complexity:  Best-case O(n^2), Worst-case O(n^2)
    """

    for i in range(len(lst) - 1):

        min_elem_index = findMinimumIndex(lst, i + 1)

        lst[i], lst[min_elem_index] = lst[min_elem_index], lst[i]

    return lst


if __name__ == "__main__":
    print(selectionSort([56, 27, 39, 4, 31, 56, 55, 27, 63, 74, 82, 77,
                              32, 32, 44]))
    print(selectionSort([5, 4, 3, 2, 1]))
