from typing import List


def my_function(x: List[int]) -> List[int]:
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
print(my_function(list(range(1, 6))))  # Add your range between the parentheses!

# print(my_function(____))  # Add your range between the parentheses!
print(my_function(list(range(1, 6))))  # Add your range between the parentheses!