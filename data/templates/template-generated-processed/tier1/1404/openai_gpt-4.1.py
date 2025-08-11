def solve():
    """Index: 1404.
    Returns: the total number of times Carson gets clawed.
    """
    # L1
    num_wombats = 9 # There are 9 wombats
    wombat_claws_per = 4 # each wombat claws him 4 times
    wombat_claws = num_wombats * wombat_claws_per

    # L2
    num_rheas = 3 # 3 rheas
    rhea_claws_per = 1 # each rhea claws him once
    rhea_claws = num_rheas * rhea_claws_per
    total_claws = wombat_claws + rhea_claws

    # FA
    answer = total_claws
    return answer