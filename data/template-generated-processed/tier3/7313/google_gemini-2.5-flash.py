def solve():
    """Index: 7313.
    Returns: the total amount of velvet James needs.
    """
    # L1
    num_hats_needed = 12 # 12 hats
    hats_per_yard = 4 # 4 hats out of one yard of velvet
    velvet_for_hats = num_hats_needed / hats_per_yard

    # L2
    num_cloaks_needed = 6 # 6 cloaks
    yards_per_cloak = 3 # three yards of velvet to make a cloak
    velvet_for_cloaks = num_cloaks_needed * yards_per_cloak

    # L3
    total_velvet_needed = velvet_for_hats + velvet_for_cloaks

    # FA
    answer = total_velvet_needed
    return answer