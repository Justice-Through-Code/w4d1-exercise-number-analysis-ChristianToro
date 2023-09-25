#number_range_analysis.py

'''
Implement Number Analysis Functions

- Function to calculate the sum of numbers within the range.
- Function to find the smallest number within the range.
- Function to find the largest number within the range.
- Function to count the number of even numbers within the range.
- Function to count the number of odd numbers within the range.

'''
# TODO: IN A COMMENT WITHIN EACH DEF, WRITE PSEUDOCODE FOR EACH SOLUTION

def calculate_sum(start, end):
    """
    Calculate the sum of numbers within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The sum of numbers within the range.
    """
    # TODO: Implement the logic to calculate the sum of numbers within the range.
    # TODO: Return the calculated sum.
    #When looking for sum of a range of integers, use the accumulator pattern. Set accumulator to 0 to initialize. The use a for loop to iterate through the range [the last value in the range is excluded, so I had to put 'end + 1'], with the accumulator being equal to itself plus each iteration. Then return the accumulator.
    accumulator = 0
    for i in range(start, end + 1):
        accumulator += i

    return accumulator

def find_smallest_number(start, end):
    """
    Find the smallest number within the specified range.

    Arguments:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The smallest number within the range.
    """
    # TODO: Implement the logic to find the smallest number within the range.
    # TODO: Return the found smallest number.
    #I wanted to figure out a way to execute this function without using the 'min()' function. 
    #We are working with a range, so set a variable 'smallest' to be equal to the starting value in the range. Technically, this is the smallest value, and we would be done with returning 'smallest'. If the numbers were not sequential, we would write a for loop using i as an iterator to iterate through the range. Nest an if statement in the for loop that sets the condition if i is less than the starting value, i is assigned to smallest. Outside of the for loop return smallest.
    smallest = start
    for i in range(start, end + 1):
        if i < start:
            i = smallest

    return smallest

def find_largest_number(start, end):
    """
    Find the largest number within the specified range.

    Args:
        start (int): The starting number of the range ( inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The largest number within the range.
    """
    # TODO: Implement the logic to find the largest number within the range.
    # TODO: Return the found largest number.
    # Instead of using the 'max()' function, I did the following.
    #We are working with a range, so set a variable 'largest' to be equal to 0. Nest an if statement in the for loop that sets the condition if i is greater than largest [assigned to 0], i is assigned to largest. Outside of the for loop return largest.
    largest = 0
    for i in range(start, end + 1):
        if i > largest:
            largest = i

    return largest



def count_even_numbers(start, end):
    """
    Count the number of even numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of even numbers within the range.
    """
    # TODO: Implement the logic to count even numbers within the range.
    # TODO: Return the count of even numbers.
    #Create a variable for even count and assign it 0. Then write a for loop to iterate through the range with i. Use a nested if state with the condition that if the remainder of i is equal to zero when divided by two, increase the even count variable by 1. Finally, return the even count.
    even_count = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            even_count += 1

    return even_count

def count_odd_numbers(start, end):
    """
    Count the number of odd numbers within the specified range.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).

    Return:
        int: The count of odd numbers within the range.
    """
    # TODO: Implement the logic to count odd numbers within the range.
    # TODO: Return the count of odd numbers.
    #Create a variable for odd count and assign it 0. Then write a for loop to iterate through the range with i. Use a nested if state with the condition that if the remainder of i is  not equal to zero when divided by two, increase the odd count variable by 1. Finally, return the odd count.

    odd_count = 0
    for i in range(start, end + 1):
        if i % 2 != 0:
            odd_count += 1

    return odd_count