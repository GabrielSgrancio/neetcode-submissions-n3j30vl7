from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    l = []
    l = arr1 + arr2
    return l

def pop_n(arr: List[int], n: int) -> List[int]:

    if n >= len(arr):
        return []
    for i in range(n, len(arr)-1):
      del arr[len(arr) - 1]
    return arr




def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    if index < 0:
        index = 0

    if index > len(arr):
        index = len(arr)

    arr += [0]  # abre um espaço no final

    for i in range(len(arr) - 1, index, -1):
        arr[i] = arr[i - 1]

    arr[index] = element

    return arr


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
