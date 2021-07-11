def get_indices_of_item_wights(arr, limit):
  array = sorted(arr)
  left=0
  right = len(arr)-1

  while left<right:
    current_sum = array[left]+array[right]
    if current_sum == limit:
      return[arr.index(array[left]),array.index(array[right])]

    elif current_sum < limit:
      left+=1
    elif current_sum > limit:
      right-=1
  return []
arr = [4,4,1]
print(get_indices_of_item_wights(arr, 5))