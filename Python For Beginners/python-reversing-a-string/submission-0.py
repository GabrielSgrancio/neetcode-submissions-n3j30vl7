def reverse_string(input_string: str) -> str:
    s = ''
    for i  in range(len(input_string)-1, -1, -1):
        s = s + input_string[i]

    return s

# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))
