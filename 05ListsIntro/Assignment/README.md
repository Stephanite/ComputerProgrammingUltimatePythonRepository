 1. `make_abc`

    Implement a function called `make_abc` that takes no input arguments. The function should return a list containing the strings "a", "b", and "c" in that order.

    | Argument | Return Value   |
    | ---------| ---------------|
    | None     | ["a", "b", "c"]|

    Checking elements on arbitrary length

1. `equal_edges`

    Implement a function called `equal_edges` that takes a list of integers as input, with a length of at least two. The function should return `True` if the first and last elements of the list are equal, and `False` otherwise.

    | Argument          | Return Value |
    | ----------------- | ------------ |
    | [1, 2, 3, 4, 1]   | `True`       |
    | [5, 6, 7, 8, 9]   | `False`      |
    | [-1, 0, 1, 2, -1] | `True`       |
    | [4, 4]            | `True`       |

1. `common_edge`

    Implement a function called `common_edge` that takes two lists of integers as input. Each list must have a length of at least two. The function should return `True` if the first or last element of the first list is equal to the first or last element of the second list, and `False` otherwise.

    | Argument 1        | Argument 2        | Return Value |
    | ----------------- | ----------------- | ------------ |
    | [1, 2, 3, 4]       | [5, 6, 7, 8]       | `False`      |
    | [1, 2, 3]          | [3, 4, 5]          | `True`       |
    | [4, 5, 6]          | [7, 8, 9]          | `False`      |
    | [-1, 0, 1, 2, -1]  | [2, 3, 4, 5]       | `False`       |
    | [3, 3, 3]          | [3, 3, 3]          | `True`       |


1. `all_the_same`

    Implement a function called `all_the_same` that takes a list of integers as input, with a length of exactly three. The function should return `True` if all three elements in the list are equal, and `False` otherwise.

    | Argument          | Return Value |
    | ----------------- | ------------ |
    | [1, 2, 3]         | `False`      |
    | [5, 5, 5]         | `True`       |
    | [-1, 0, 1]        | `False`      |
    | [3, 3, 3]         | `True`       |
    | [4, 5, 6]         | `False`      |


1. `all_unique`

    Implement a function called `all_unique` that takes a list of integers as input, with a length of exactly three. The function should return `True` if all three elements in the list are different, and `False` otherwise.

    | Argument          | Return Value |
    | ----------------- | ------------ |
    | [1, 2, 3]         | `True`       |
    | [5, 5, 5]         | `False`      |
    | [-1, 0, 1]        | `True`       |
    | [3, 3, 3]         | `False`      |
    | [4, 5, 6]         | `True`       |


1. `increasing`

    Implement a function called `increasing` that takes a list of integers as input, with a length of exactly three. The function should return `True` if the elements in the list are in strictly increasing order, and `False` otherwise.

    | Argument          | Return Value |
    | ----------------- | ------------ |
    | [1, 2, 3]         | `True`       |
    | [5, 5, 5]         | `False`      |
    | [-1, 0, 1]        | `True`       |
    | [3, 3, 3]         | `False`      |
    | [4, 5, 6]         | `True`       |

1. `all_true`

    Implement a function called `all_true` that takes a list of booleans as input, with a length of exactly three. The function should return `True` if all three elements in the list are `True`, and `False` otherwise.

    | Argument             | Return Value |
    | -------------------- | ------------ |
    | [True, False, True]  | `False`      |
    | [False, False, False]| `False`      |
    | [True, True, True]   | `True`       |
    | [False, True, False] | `False`      |
    | [True, False, False] | `False`      |


1. `mostly_true`

    Implement a function called `mostly_true` that takes a list of booleans as input, with a length of exactly three. The function should return `True` if at least two elements in the list are `True`, and `False` otherwise.

    | Argument             | Return Value |
    | -------------------- | ------------ |
    | [True, False, True]  | `True`       |
    | [False, False, False]| `False`      |
    | [True, True, True]   | `True`       |
    | [False, True, False] | `True`       |
    | [True, False, False] | `False`      |



-   sum3(l1)
-   has_negative(l1)

Modifying list
-   make_copy(nums1)
-   repeat_thrice(num1)
-   make_reversed_copy(nums)
-   reverse_in_place(nums)
-   zip_together(l1, l2)