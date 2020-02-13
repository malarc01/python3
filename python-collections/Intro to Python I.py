# List = group of items we reference by index
# - mutable
# - duplicate items

# Mutable vs immutable

# create it
my_colors = ['red', 'orange', 'yellow']


# add vs insert
my_colors.append('green')  # add to end
my_colors.insert(2, "blue")


# remove vs. pop vs. del
my_colors.remove("orange")  # removes item
my_colors.pop()  # removes last item
del my_colors[1]  # removes item at i

# traverse
for i in range(0, len(my_colors)):
    print(my_colors[i])
    # access an item
print(my_colors)


# List Slices
my_colors = ["red", "yellow", "orange"]

# 1st item you want: 1st item you DO NOT want
primary_colors = my_colors[0:2]

# 1st item you want: (goes to end)
primary_colors = my_colors[1:]

# 1st item you DO NOT want: (starts at beginning)
primary_colors = my_colors[:2]


# List Comprehensions

my_colors = ["red", "yellow", "orange", "blue", "green"]

# return new list of colors with less # than 5 chars
new_colors = [c for c in my_colors if len(c) < 5]
