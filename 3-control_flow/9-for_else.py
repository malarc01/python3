successful = True


for number in range(3):
    print("Attempt")
    if successful:
        print("Success")
        break
else:
    print("Attempted 3 times & failed")