def binary_search(array, target):
  l, h = 0, len(array) - 1
  idx = -1

  while l <= h:
    m = (l + h) // 2
    mid = array[m]
    
    if target < mid:
      h = m - 1
    elif target > mid:
      l = m + 1
    else:
      return m
  return -1

arr = [1, 2, 4, 7, 8, 16]
print(binary_search(arr, 0))
