# Last in - First Out
# browser back button
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

print(browsing_session)

last = browsing_session.pop()
print(last)

if not browsing_session:
    print("disable")

print(browsing_session)
print("redirect", browsing_session[-1])