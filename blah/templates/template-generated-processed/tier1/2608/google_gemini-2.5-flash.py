def solve():
    """Index: 2608.
    Returns: the number of additional slices of ham needed.
    """
    # L1
    slices_per_sandwich = 3 # three slices of ham in each sandwich
    num_sandwiches = 50 # 50 ham sandwiches
    total_slices_needed = slices_per_sandwich * num_sandwiches

    # L2
    slices_on_hand = 31 # 31 slices of ham
    additional_slices_needed = total_slices_needed - slices_on_hand

    # FA
    answer = additional_slices_needed
    return answer