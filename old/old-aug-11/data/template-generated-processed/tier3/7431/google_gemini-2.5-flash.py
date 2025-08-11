def solve():
    """Index: 7431.
    Returns: the number of campers that can be fed.
    """
    # L1
    num_bass = 6 # six two-pound bass
    weight_per_bass = 2 # six two-pound bass
    total_bass_weight = num_bass * weight_per_bass

    # L2
    num_salmon = 2 # two twelve-pound salmon
    weight_per_salmon = 12 # two twelve-pound salmon
    total_salmon_weight = num_salmon * weight_per_salmon

    # L3
    trout_weight = 8 # an eight-pound trout
    total_fish_weight = trout_weight + total_bass_weight + total_salmon_weight

    # L4
    pounds_per_camper = 2 # If each person will eat two pounds of fish
    num_campers_fed = total_fish_weight / pounds_per_camper

    # FA
    answer = num_campers_fed
    return answer