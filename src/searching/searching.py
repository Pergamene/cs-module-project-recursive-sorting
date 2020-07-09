import math

# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
  if start > end:
    return -1
  mid = math.floor((start + end) / 2)
  if arr[mid] < target:
    return binary_search(arr, target, mid+1, end)
  if arr[mid] > target:
    return binary_search(arr, target, start, mid-1)
  return mid

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
  left = 0
  right = len(arr) - 1
  isAssending = arr[left] < arr[right]
  while left <= right:
    mid = math.floor((left + right) / 2)
    if arr[mid] == target:
      return mid
    if (isAssending):
      if arr[mid] > target:
        right = mid - 1
      else:
        left = mid + 1
    else:
      if arr[mid] < target:
        right = mid - 1
      else:
        left = mid + 1
  return -1
