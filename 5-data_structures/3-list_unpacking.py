numbers = [1,2,3,4,4,4,4,4,]
first,*other,last, = numbers

print(first,last)
print(other)

def multiply (*numbers):
    print(numbers)

multiply(1,2,3,4,5)

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

