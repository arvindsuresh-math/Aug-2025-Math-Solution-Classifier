def solve():
    """Index: 771.
    Returns: the number of packs of bread Jimmy needs to buy.
    """
    # L1
    num_sandwiches = 8 # He makes 8 sandwiches in total
    slices_per_sandwich = 2 # using two slices of bread each
    total_slices_needed = num_sandwiches * slices_per_sandwich

    # L2
    slices_per_pack = 4 # each pack has 4 slices of bread in it
    packs_needed = total_slices_needed / slices_per_pack

    # FA
    answer = packs_needed
    return answer