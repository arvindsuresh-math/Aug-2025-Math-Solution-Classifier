def solve():
    """Index: 6909.
    Returns: the number of carpenters needed.
    """
    # L1
    target_chairs = 75 # 75 chairs
    initial_chairs = 50 # 50 chairs
    chairs_ratio = target_chairs / initial_chairs

    # L2
    initial_carpenters = 8 # 8 carpenters
    needed_carpenters = initial_carpenters * chairs_ratio

    # FA
    answer = needed_carpenters
    return answer