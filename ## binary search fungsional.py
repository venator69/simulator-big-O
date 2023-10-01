import random

# Function to create a random sorted list
def createRandomSortedList(num, start, end):
    arr = []
    
    while len(arr) < num:
        tmp = random.randint(start, end)
        if tmp not in arr:
            arr.append(tmp)
    
    arr.sort()
    
    return arr

# Binary search function
def binary_search(target, arr, start, end, count):
    if start > end:
        print(f"Array hasn't been sorted yet")
        return count
    else:
        mid = (start + end) // 2
        if arr[mid] == target:
            print(f"Found {target} at index {mid}")
            return (count)
        elif arr[mid] > target:
            count += 1
            return binary_search(target, arr, start, mid - 1, count)
        elif arr[mid] < target:
            count += 1
            return binary_search(target, arr, mid + 1, end, count)
        else:
            print(f"There's no {target} in the array")

# linear search algorithm
def linear_search(target, arr, count):
    count = 0
    for idx, num in enumerate(arr):
        if num == target:
            print(f"Found {target} at index {idx}")
            return count
        count += 1
    print(f"There's no {target} in the array")
    return count

# Generate a random sorted list
randarray = createRandomSortedList(16, 1, 20)


number =random.randint(0,20)
# Perform binary search
binary_count = binary_search(number, randarray, 0, 15, 1)
print(f"Total recursive calls in binary search: {binary_count}")

# Perform basic search
basic_count = linear_search(number, randarray, 0)
print(f"Total recursive calls in basic search: {basic_count}")
j