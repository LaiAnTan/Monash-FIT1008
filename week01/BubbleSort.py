
def naiveBubbleSort(lst):

    """
    Naive Bubble Sort algorithm.

    Sorts elements by swapping the position of two elements if they are in the
    wrong order.

    :param lst: list to be sorted.
    :return lst: the sorted list.
    :complexity:  Best-case O(n^2), Worst-case O(n^2)
    """

    for _ in range(len(lst) - 1):

        for i in range(len(lst) - 1):

            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]  # swap elements

    return lst


def optimisedBubbleSort(lst):

    """
    The optimised version of Bubble Sort algorithm.

    Optimizations:

    1. Only checks for unsorted elements up until a flag, which marks the
    boundary between unsorted (potentially) and sorted elements.

    2. Breaks out of the loop if no elements were swapped, as we can infer that
    the list is sorted if no elements' positions' changed in a single
    iteration.
    
    :param lst: list to be sorted.
    :return lst: the sorted list.
    :complexity:  Best-case O(n), Worst-case O(n^2)
    """

    for i in range(len(lst) - 1):

        swapped = False

        for j in range(len(lst) - 1 - i):  # refer optimisation 1

            if lst[j] > lst[j + 1]:

                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # swap elements
                swapped = True

        if not swapped:  # refer optimisation 2
            break

    return lst


if __name__ == "__main__":
    print(naiveBubbleSort([5, 4, 3, 2, 1]))
    print(optimisedBubbleSort([5, 4, 3, 2, 1]))
