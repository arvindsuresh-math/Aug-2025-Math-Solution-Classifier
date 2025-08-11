def solve():
    """Index: 2189.
    Returns: the total weight Tom was moving with.
    """
    # L1
    tom_weight = 150 # Tom weighs 150 kg
    weight_multiplier_per_hand = 1.5 # 1.5 times his weight in each hand
    weight_in_each_hand = tom_weight * weight_multiplier_per_hand

    # L2
    num_hands = 2 # WK
    total_weight_in_hands = weight_in_each_hand * num_hands

    # L3
    vest_weight_multiplier = 0.5 # weighing half his weight
    vest_weight = tom_weight * vest_weight_multiplier

    # L4
    total_weight_moved = total_weight_in_hands + vest_weight

    # FA
    answer = total_weight_moved
    return answer