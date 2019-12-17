letters = ["a","b","c"]

# Add
letters.append("d")
letters.insert(0,"-")
# remove
letters.pop(0) # pass index to remove
letters.remove("b")

# deletes a range of items
# del letters[0:3]
letters.clear()

print(letters)
