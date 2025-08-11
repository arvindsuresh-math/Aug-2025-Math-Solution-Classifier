def solve():
    """Index: 3012.
    Returns: the number of slices of cake left over.
    """
    # L1
    num_friends = 8 # invited 8 friends
    slices_per_friend = 2 # each one will want two slices of cake
    friends_slices_eaten = num_friends * slices_per_friend

    # L2
    amber_eats = 3 # she eats three herself
    total_slices_eaten = friends_slices_eaten + amber_eats

    # L3
    num_cakes_baked = 4 # she bakes 4 cakes
    slices_per_cake = 6 # Each cake makes 6 slices
    total_slices_made = num_cakes_baked * slices_per_cake

    # L4
    slices_left_over = total_slices_made - total_slices_eaten

    # FA
    answer = slices_left_over
    return answer