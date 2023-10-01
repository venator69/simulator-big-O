import random

# Binary search function
def binary_search(target, start, end, count):
    mid = (start + end) // 2
    if mid == target:

        return (mid, count)
    elif mid > target:
        count += 1
        return binary_search(target, start, mid - 1, count)
    else:
        count += 1
        return binary_search(target, mid + 1, end, count)

# Creating the simulator
def sim(sampling, x):
    arrsample = [(0, 0) for _ in range(sampling)]
    for i in range(sampling):
        target = random.randint(0, x - 1)
        result = binary_search(target, 0, x - 1, 1)
        arrsample[i] = result
    return arrsample

print(sim(10, 64))
