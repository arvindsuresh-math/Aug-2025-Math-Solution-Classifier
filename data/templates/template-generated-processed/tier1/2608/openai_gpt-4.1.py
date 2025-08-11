def solve():
    """Index: 2608.
    Returns: the number of additional slices of ham Anna needs to make 50 sandwiches.
    """
    # L1
    slices_per_sandwich = 3 # three slices of ham in each sandwich
    num_sandwiches = 50 # make 50 ham sandwiches
    total_needed = slices_per_sandwich * num_sandwiches

    # L2
    slices_on_hand = 31 # she has 31 slices of ham
    more_needed = total_needed - slices_on_hand

    # FA
    answer = more_needed
    return answer