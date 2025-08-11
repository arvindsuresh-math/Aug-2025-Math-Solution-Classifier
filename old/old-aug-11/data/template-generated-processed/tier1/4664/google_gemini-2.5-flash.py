def solve():
    """Index: 4664.
    Returns: the number of slices of pizza left for Phill.
    """
    # L1
    initial_pizzas = 1 # 1 pizza
    cut_in_half_multiplier = 2 # cutting it in half
    slices_after_first_cut = initial_pizzas * cut_in_half_multiplier

    # L2
    slices_after_second_cut = slices_after_first_cut * cut_in_half_multiplier

    # L3
    total_slices_initial = slices_after_second_cut * cut_in_half_multiplier

    # L4
    slices_per_friend_group1 = 2 # 2 slices
    num_friends_group1 = 2 # 2 of his friends
    slices_given_group1 = slices_per_friend_group1 * num_friends_group1

    # L5
    slices_per_friend_group2 = 1 # 1 slice
    num_friends_group2 = 3 # 3 others
    slices_given_group2 = slices_per_friend_group2 * num_friends_group2
    total_slices_handed_out = slices_given_group2 + slices_given_group1

    # L6
    slices_remaining = total_slices_initial - total_slices_handed_out

    # FA
    answer = slices_remaining
    return answer