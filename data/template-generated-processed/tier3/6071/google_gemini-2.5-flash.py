def solve():
    """Index: 6071.
    Returns: the total number of calories Bob ate.
    """
    # L1
    total_slices = 8 # pizza with 8 slices
    eaten_fraction_denominator = 2 # eats half of it
    slices_eaten = total_slices / eaten_fraction_denominator

    # L2
    calories_per_slice = 300 # each slice was 300 calories
    total_calories_eaten = slices_eaten * calories_per_slice

    # FA
    answer = total_calories_eaten
    return answer