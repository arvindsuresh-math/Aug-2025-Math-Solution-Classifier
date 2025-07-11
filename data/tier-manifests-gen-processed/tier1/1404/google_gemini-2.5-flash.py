def solve():
    """Index: 1404.
    Returns: the total number of times Carson gets clawed.
    """
    # L1
    num_wombats = 9 # 9 wombats
    claws_per_wombat = 4 # each wombat claws him 4 times
    total_wombat_claws = num_wombats * claws_per_wombat

    # L2
    num_rheas = 3 # 3 rheas
    claws_per_rhea = 1 # each rhea claws him once
    total_rhea_claws = num_rheas * claws_per_rhea
    total_claws = total_wombat_claws + total_rhea_claws

    # FA
    answer = total_claws
    return answer