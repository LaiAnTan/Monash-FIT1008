
# this does not use slides implementation lol
def insertionSort(lst):

    """
    Naive Insertion Sort Algorithm.

    Sorts the elements by shifting elements to the left until they reach their
    correct positions in a sorted list.
    
    :param lst: list to be sorted.
    :return lst: the sorted list.
    :complexity: Best-case O(n), Worst-case O(n^2)
    """

    for i in range(len(lst)):

        j = i

        while j > 0 and lst[j - 1] > lst[j]:

            lst[j], lst[j - 1] = lst[j - 1], lst[j]  # swap elements

            j -= 1

    return lst


if __name__ == "__main__":
    print(insertionSort([56, 27, 39, 4, 31, 56, 55, 27, 63, 74, 82, 77,
                              32, 32, 44]))
    print(insertionSort([5, 4, 3, 2, 1]))
