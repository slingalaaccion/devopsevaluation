def sum_of_consecutive_multiples(X):
  """
  Calculates the sum of X, XX, XXX, and XXXX where X is a single decimal digit.

  Args:
    X: A single decimal digit (0-9).

  Returns:
    The sum of X, XX, XXX, and XXXX.

  Raises:
    ValueError: If X is not a single decimal digit or is not a number.
  """

  try:
    X = int(X)
  except ValueError:
    raise ValueError("Invalid input. X must be a single decimal digit.")

  if not 0 <= X <= 9:
    raise ValueError("Invalid input. X must be a single decimal digit between 0 and 9.")

  XX = int(str(X) * 2)
  XXX = int(str(X) * 3)
  XXXX = int(str(X) * 4)

  return X + XX + XXX + XXXX

user_input = input("Enter a single decimal digit:")
try:
  result = sum_of_consecutive_multiples(user_input)
  XX = int(str(user_input) * 2)
  XXX = int(str(user_input) * 3)
  XXXX = int(str(user_input) * 4)
  print(f"The sum of decimal dight {user_input} decimal tranformation is: {result}") 
except ValueError as e:
  print(f"Error: {e}")

