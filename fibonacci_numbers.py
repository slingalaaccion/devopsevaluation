# Fibonacci Numbers.py

def sum_of_even_fibonacci_numbers(limit):
  """
  Calculates the sum of the first 'limit' even-valued Fibonacci numbers.

  Args:
    limit: The number of even-valued Fibonacci numbers to sum.

  Returns:
    The sum of the first 'limit' even-valued Fibonacci numbers.

  Raises:
    ValueError: If 'limit' is not a positive integer.
  """

  if not isinstance(limit, int) or limit <= 0:
    raise ValueError("Limit must be a positive integer.")

  a, b = 0, 2  # Start with the first two even Fibonacci numbers (0 and 2)
  sum_even_fib = 2  # Initialize sum with the first even number
  count = 1  # Counter for even Fibonacci numbers

  while count < limit:
    # Calculate the next even Fibonacci number
    c = 4 * b + a
    a, b = b, c
    sum_even_fib += c
    count += 1

  return sum_even_fib

if __name__ == "__main__":
  try:
    limit = int(input("Enter the number of even-valued Fibonacci numbers to sum: "))
    result = sum_of_even_fibonacci_numbers(limit)
    print(f"Sum of the first {limit} even-valued Fibonacci numbers: {result}")
  except ValueError as e:
    print(f"Error: {e}")
