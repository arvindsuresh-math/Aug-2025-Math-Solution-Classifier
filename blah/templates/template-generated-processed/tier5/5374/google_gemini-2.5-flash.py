def solve():
    """Index: 5374.
    Returns: the total number of marbles in the jar.
    """
    # L3
    remaining_fraction = 0.25 # Derived from: 1 (total) - 0.5 (blue) - 0.25 (red) = 0.25
    green_marbles = 27 # 27 of them are green
    yellow_marbles = 14 # 14 of them are yellow
    green_plus_yellow_marbles = green_marbles + yellow_marbles

    # L4
    # The solution implies that green and yellow marbles constitute 25% of the total.
    # To find the total, we multiply the sum of green and yellow marbles by 1 / 0.25 = 4.
    multiplier_from_percentage = 4 # Derived from 1 / remaining_fraction
    total_marbles = multiplier_from_percentage * green_plus_yellow_marbles

    # FA
    answer = total_marbles
    return answer