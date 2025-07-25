def solve():
    """Index: 6987.
    Returns: the total number of fish in the river now.
    """
    # L1
    initial_salmon = 500 # 500 salmons initially
    increase_multiplier = 10 # ten times the number initially
    new_salmon_migrated = initial_salmon * increase_multiplier

    # L2
    total_salmon_now = new_salmon_migrated + initial_salmon

    # FA
    answer = total_salmon_now
    return answer