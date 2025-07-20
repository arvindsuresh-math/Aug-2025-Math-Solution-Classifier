def solve():
    """Index: 5470.
    Returns: the difference between broken spiral shells and perfect spiral shells.
    """
    # L1
    broken_shells = 52 # 52 broken shells
    half_divisor = 2 # half of them were spiral
    broken_spiral_shells = broken_shells / half_divisor

    # L2
    perfect_shells = 17 # 17 perfect shells
    not_spiral_perfect_shells = 12 # 12 of them were not spiral
    perfect_spiral_shells = perfect_shells - not_spiral_perfect_shells

    # L3
    difference_in_spiral_shells = broken_spiral_shells - perfect_spiral_shells

    # FA
    answer = difference_in_spiral_shells
    return answer