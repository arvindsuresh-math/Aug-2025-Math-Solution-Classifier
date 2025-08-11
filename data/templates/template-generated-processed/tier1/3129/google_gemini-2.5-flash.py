def solve():
    """Index: 3129.
    Returns: the total money Mike spent on plants for himself.
    """
    # L1
    total_rose_bushes = 6 # 6 rose bushes
    rose_bushes_for_friend = 2 # 2 of them are for his friend
    rose_bushes_for_self = total_rose_bushes - rose_bushes_for_friend

    # L2
    cost_per_rose_bush = 75 # 75 dollars each
    cost_rose_bushes_for_self = rose_bushes_for_self * cost_per_rose_bush

    # L3
    num_aloes = 2 # 2 tiger tooth aloes
    cost_per_aloe = 100 # 100 dollars each
    cost_aloes = num_aloes * cost_per_aloe

    # L4
    total_spent = cost_aloes + cost_rose_bushes_for_self

    # FA
    answer = total_spent
    return answer