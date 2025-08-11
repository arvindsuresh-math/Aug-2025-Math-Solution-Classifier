def solve():
    """Index: 1378.
    Returns: Mel's weight.
    """
    # L3
    brenda_weight = 220 # Brenda weighs 220 pounds
    additional_weight = 10 # 10 pounds more
    multiplier_for_mel = 3 # 3 times Mel's weight
    three_times_mel_weight = brenda_weight - additional_weight

    # L4
    mel_weight = three_times_mel_weight / multiplier_for_mel

    # FA
    answer = mel_weight
    return answer