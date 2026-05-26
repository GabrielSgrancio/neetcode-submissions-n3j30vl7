from typing import List

def read_integers() -> List[int]:
    ls = []
    integers = (input())
    ln = integers.split(",")
    for i in ln:
        ls.append(int(i))
    return ls
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
