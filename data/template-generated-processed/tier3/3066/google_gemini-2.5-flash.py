def solve():
    """Index: 3066.
    Returns: the initial number of fruits Martin had.
    """
    # L1
    oranges_now = 50 # If he has 50 oranges now
    limes_ratio_divisor = 2 # twice as many oranges as limes
    limes_now = oranges_now / limes_ratio_divisor

    # L2
    fruits_now = oranges_now + limes_now

    # L3
    initial_fruits_multiplier = 2 # After eating half of the number of fruits
    initial_fruits = initial_fruits_multiplier * fruits_now

    # FA
    answer = initial_fruits
    return answer