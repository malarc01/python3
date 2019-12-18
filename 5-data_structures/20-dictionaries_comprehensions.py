values = []
for x in range(5):
    values.append(x*2)

values = {}
for x in range(5):
    values[x] = x*2

# [expression for item in items]
# same code as above but for succint
valuez = [x*2 for x in range(5)]
# not limited to list
vals = {x: x*2 for x in range(5)}

v = (x*2 for x in range(5))

print(v)
