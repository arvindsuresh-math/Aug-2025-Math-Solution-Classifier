def solve():
    """Index: 5653.
    Returns: the combined weight of the two siblings.
    """
    # L1
    antonio_weight = 50 # weight is 50 kilograms
    sister_less_than_antonio = 12 # weighs 12 kilograms less than him
    sister_weight = antonio_weight - sister_less_than_antonio

    # L2
    total_weight = antonio_weight + sister_weight

    # FA
    answer = total_weight
    return answer