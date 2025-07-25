def solve():
    """Index: 4023.
    Returns: the number of bananas Vivian needs to buy.
    """
    # L1
    num_yogurts = 5 # make 5 yogurts
    slices_per_yogurt = 8 # topped with 8 banana slices
    total_slices_needed = num_yogurts * slices_per_yogurt

    # L2
    slices_per_banana = 10 # One banana will yield 10 slices
    bananas_to_buy = total_slices_needed / slices_per_banana

    # FA
    answer = bananas_to_buy
    return answer