def solve():
    """Index: 7430.
    Returns: the number of available spaces on the benches.
    """
    # L1
    num_benches = 50 # 50 benches
    capacity_per_bench = 4 # capacity of 4 people each
    total_capacity = num_benches * capacity_per_bench

    # L2
    people_sitting = 80 # 80 people were sitting on the benches
    empty_spaces = total_capacity - people_sitting

    # FA
    answer = empty_spaces
    return answer