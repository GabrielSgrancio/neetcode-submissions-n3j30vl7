from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    tmp_stack = []
    while len(arr) > 0:
        tmp_stack.append(arr[-1])
        del arr[-1]
    return tmp_stack

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
