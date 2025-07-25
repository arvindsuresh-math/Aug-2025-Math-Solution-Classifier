def solve():
    """Index: 336.
    Returns: the number of slices of cake left.
    """
    # L1
    num_cakes = 2 # Alex has 2 cakes
    slices_per_cake = 8 # each cut into 8 slices
    total_slices = num_cakes * slices_per_cake

    # L2
    given_away_fraction_denominator = 4 # A fourth of the slices
    slices_given_to_friends = total_slices / given_away_fraction_denominator

    # L3
    slices_after_friends = total_slices - slices_given_to_friends

    # L4
    family_fraction_denominator = 3 # A third of the remaining slices
    slices_given_to_family = slices_after_friends / family_fraction_denominator

    # L5
    alex_eats_slices = 3 # Alex eats 3 slices
    remaining_slices = slices_after_friends - slices_given_to_family - alex_eats_slices

    # FA
    answer = remaining_slices
    return answer