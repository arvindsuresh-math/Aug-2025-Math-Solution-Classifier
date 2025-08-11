def solve():
    """Index: 5673.
    Returns: the number of slices of pizza left.
    """
    # L1
    john_ate_slices = 3 # John ate 3 slices
    sam_multiplier = 2 # twice the amount
    sam_ate_slices = john_ate_slices * sam_multiplier

    # L2
    total_eaten_slices = john_ate_slices + sam_ate_slices

    # L3
    total_pizza_slices = 12 # pre-sliced into 12 pieces
    slices_left = total_pizza_slices - total_eaten_slices

    # FA
    answer = slices_left
    return answer