def get_integer_array(prompt):
  """
  Gets an array of integers from user input, handling invalid input.

  Args:
    prompt: The message to display to the user.

  Returns:
    A list of integers entered by the user.
  """
  while True:
    try:
      array_str = input(prompt)
      array = [int(x) for x in array_str.split()]
      return array
    except ValueError:
      print("Invalid input. Please enter space-separated integers only.")

def find_common_elements(arr1, arr2):
  """
  Finds common elements in two sorted arrays.

  Args:
    arr1: The first sorted array of integers.
    arr2: The second sorted array of integers.

  Returns:
    A list containing the common elements without duplicates.
  """

  result = []
  i = 0
  j = 0

  while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]:
      if not result or result[-1] != arr1[i]:
        result.append(arr1[i])
      i += 1
      j += 1
    elif arr1[i] < arr2[j]:
      i += 1
    else:
      j += 1

  return result

# Get input from the user
arr1 = get_integer_array("Enter the elements of the first array (space-separated): ")
arr2 = get_integer_array("Enter the elements of the second array (space-separated): ")

arr1.sort()
arr2.sort()

# Find and print common elements
common_elements = find_common_elements(arr1, arr2)
print("Common elements:", common_elements)