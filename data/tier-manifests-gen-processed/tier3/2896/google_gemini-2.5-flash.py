def solve():
    """Index: 2896.
    Returns: the weight of each cut piece of the log.
    """
    # L1
    log_length = 20 # a 20-foot log
    cut_divisor = 2 # cuts it in half
    piece_length = log_length / cut_divisor

    # L2
    weight_per_foot = 150 # each linear foot of the log weighs 150 pounds
    piece_weight = piece_length * weight_per_foot

    # FA
    answer = piece_weight
    return answer