def solve():
    """Index: 6792.
    Returns: the difference in the dogs' weight at the end of the year.
    """
    # L1
    labrador_start_weight = 40 # labrador puppy weighs 40 pounds
    weight_gain_percent_num = 25 # gains 25% of their starting weight
    percent_factor = 0.01 # WK
    labrador_gain_weight = labrador_start_weight * weight_gain_percent_num * percent_factor

    # L2
    labrador_end_weight = labrador_start_weight + labrador_gain_weight

    # L3
    dachshund_start_weight = 12 # dachshund puppy weighs 12 pounds
    dachshund_gain_weight = dachshund_start_weight * weight_gain_percent_num * percent_factor

    # L4
    dachshund_end_weight = dachshund_start_weight + dachshund_gain_weight

    # L5
    weight_difference = labrador_end_weight - dachshund_end_weight

    # FA
    answer = weight_difference
    return answer