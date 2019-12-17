numbers = [1,1,2,3,4]
first = set(numbers)
second = {1,5}
# second.add(5)
# second.remove(5)
# len(second)


# union of sets thtat all item in either first or second set
print(first | second) 


# new set that are in BOTH sets
print(first & second)
# difference btwn sets
print(first-second)

# symmetric difference returns first or second set but not both
print(first^second)
# unordered collections => can not access using an index


if 1 in first:
    print("yes")
# print(first[0])

name

