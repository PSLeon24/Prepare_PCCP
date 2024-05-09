import time

n = int(input("Number of elements: "))
haystack = [i for i in range(n)]

print("Searching for the maximum element in the list")
ts = time.time()
maximum = max(haystack)
elasped = time.time() - ts

print(f"Maximum element is: {maximum}, Elasped time: {elasped}")
