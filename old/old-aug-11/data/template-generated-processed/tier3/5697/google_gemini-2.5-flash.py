def solve():
    """Index: 5697.
    Returns: the number of slices of bread remaining.
    """
    # L1
    total_slices = 12 # sliced it into 12 pieces
    breakfast_divisor = 3 # a third of the bread slices
    eaten_for_breakfast = total_slices / breakfast_divisor

    # L2
    remaining_after_breakfast = total_slices - eaten_for_breakfast

    # L3
    lunch_slices = 2 # used 2 bread slices
    remaining_after_lunch = remaining_after_breakfast - lunch_slices

    # FA
    answer = remaining_after_lunch
    return answer