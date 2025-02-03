def list_divide(numbers, divide=2):
    count = 0  # Counter for divisible numbers
    for num in numbers:  # Loop through the list
        if num % divide == 0:  # Check divisibility
            count += 1  # Increment counter if divisible
    return count  # Return the final count

class ListDivideException(Exception):
    pass  # Custom exception class (no additional functionality needed)

def test_list_divide():
    # Define test cases and expected outputs
    test_cases = [
        ([1, 2, 3, 4, 5], 2, 2),
        ([2, 4, 6, 8, 10], 2, 5),
        ([30, 54, 63, 98, 100], 10, 2),
        ([], 2, 0),
        ([1, 2, 3, 4, 5], 1, 5)
    ]

    # Loop through each test case
    for numbers, divide, expected in test_cases:
        result = list_divide(numbers, divide)  # Call the function
        if result != expected:  # Check if the result matches expected output
            raise ListDivideException(f"Test failed for input {numbers} with divide={divide}. Expected {expected}, but got {result}")

# Call test function when script runs
test_list_divide()

