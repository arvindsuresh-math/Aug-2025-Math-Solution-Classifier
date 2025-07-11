def solve():
    """Index: 336.
    Returns: the number of slices of cake Alex has left.
    """
    # L1
    cakes = 2 # Alex has 2 cakes
    slices_per_cake = 8 # each cut into 8 slices
    total_slices = cakes * slices_per_cake

    # L2
    friends_divisor = 4 # A fourth of the slices
    slices_given_to_friends = total_slices / friends_divisor

    # L3
    slices_after_friends = total_slices - slices_given_to_friends

    # L4
    family_divisor = 3 # A third of the remaining slices
    slices_given_to_family = slices_after_friends / family_divisor

    # L5
    alex_eats = 3 # Alex eats 3 slices
    slices_left = slices_after_friends - slices_given_to_family - alex_eats

    # FA
    answer = slices_left
    return answer