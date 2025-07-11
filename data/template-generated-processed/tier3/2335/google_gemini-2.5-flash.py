def solve():
    """Index: 2335.
    Returns: the number of slices of bread each friend ate.
    """
    # L1
    slices_per_loaf = 15 # A loaf of bread was sliced into 15
    num_loaves = 4 # 4 loaves of bread
    total_slices = slices_per_loaf * num_loaves

    # L2
    num_friends = 10 # Ten friends
    slices_per_friend = total_slices / num_friends

    # FA
    answer = slices_per_friend
    return answer