def solve():
    """Index: 7267.
    Returns: the number of slices James eats.
    """
    # L1
    initial_slices = 8 # an 8 piece pizza
    friend_eats = 2 # His friend eats 2 slices
    slices_left_after_friend = initial_slices - friend_eats

    # L2
    james_eats_divisor = 2 # James eats half of what is left
    james_eats_slices = slices_left_after_friend / james_eats_divisor

    # FA
    answer = james_eats_slices
    return answer