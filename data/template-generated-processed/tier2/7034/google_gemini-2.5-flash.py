def solve():
    """Index: 7034.
    Returns: the total pounds of fish caught.
    """
    # L1
    num_trout = 4 # 4 trout
    trout_weight_per_fish = 2 # trout weigh 2 pounds each
    trout_total_weight = num_trout * trout_weight_per_fish

    # L2
    num_catfish = 3 # 3 catfish
    catfish_weight_per_fish = 1.5 # catfish weigh 1.5 pounds each
    catfish_total_weight = num_catfish * catfish_weight_per_fish

    # L3
    num_bluegills = 5 # 5 bluegills
    bluegill_weight_per_fish = 2.5 # bluegills weigh 2.5 pounds each
    bluegill_stated_weight_text = 7.5 # from solution text: 7.5 pounds of bluegill
    bluegill_calculated_weight = num_bluegills * bluegill_weight_per_fish

    # L4
    total_fish_stated_weight_text = 20 # from solution text: 20 pounds of fish
    total_fish_calculated_weight = trout_total_weight + catfish_total_weight + bluegill_calculated_weight

    # FA
    answer = total_fish_calculated_weight
    return answer