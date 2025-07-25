def solve():
    """Index: 2210.
    Returns: the number of packs John needs to buy.
    """
    # L1
    utensils_per_pack = 30 # They come in 30 packs with an equal number of knives, forks, and spoons
    types_of_utensils = 3 # WK
    spoons_per_pack = utensils_per_pack / types_of_utensils

    # L2
    desired_spoons = 50 # he wants 50 spoons
    packs_needed = desired_spoons / spoons_per_pack

    # FA
    answer = packs_needed
    return answer