n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

# print(flatten(n))
def flatten(lst):
    new_list = []
    for i in lst:
        for j in i:
            new_list.append(j)
    return new_list

print(flatten(n))