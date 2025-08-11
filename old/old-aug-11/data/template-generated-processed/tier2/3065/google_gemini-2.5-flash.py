def solve():
    """Index: 3065.
    Returns: the total weight Tom can hold.
    """
    # L1
    initial_weight_per_hand = 80 # 80 kg farmer handles per hand
    doubling_factor = 2 # WK
    weight_after_doubling_per_hand = initial_weight_per_hand * doubling_factor

    # L2
    specialization_percent_decimal = 0.1 # extra 10%
    specialization_gain_per_hand = weight_after_doubling_per_hand * specialization_percent_decimal

    # L3
    total_weight_per_hand = weight_after_doubling_per_hand + specialization_gain_per_hand

    # L4
    num_hands = 2 # WK
    total_weight_both_hands = total_weight_per_hand * num_hands

    # FA
    answer = total_weight_both_hands
    return answer