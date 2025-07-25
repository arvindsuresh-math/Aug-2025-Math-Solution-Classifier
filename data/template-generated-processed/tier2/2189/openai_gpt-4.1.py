def solve():
    """Index: 2189.
    Returns: the total weight Tom was moving with.
    """
    # L1
    tom_weight = 150 # Tom weighs 150 kg
    hand_multiplier = 1.5 # 1.5 times his weight in each hand
    hand_weight = tom_weight * hand_multiplier

    # L2
    hands_count = 2 # each hand (2 hands)
    total_hand_weight = hand_weight * hands_count

    # L3
    vest_multiplier = 0.5 # weight vest weighing half his weight
    vest_weight = tom_weight * vest_multiplier

    # L4
    total_weight = total_hand_weight + vest_weight

    # FA
    answer = total_weight
    return answer