def solve():
    """Index: 7299.
    Returns: the number of leaves dropped on the fifth day.
    """
    # L1
    initial_leaves = 340 # If it had 340 leaves
    fraction_denominator = 10 # a tenth of its initial quantity of leaves
    leaves_per_day = initial_leaves / fraction_denominator

    # L2
    num_days = 4 # over the course of four days
    leaves_first_four_days = leaves_per_day * num_days

    # L3
    leaves_fifth_day = initial_leaves - leaves_first_four_days

    # FA
    answer = leaves_fifth_day
    return answer