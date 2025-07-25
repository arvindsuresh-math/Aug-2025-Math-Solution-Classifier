def solve():
    """Index: 6683.
    Returns: the percentage of apples in the basket.
    """
    # L1
    initial_apples = 10 # 10 apples
    initial_oranges = 5 # 5 oranges
    added_oranges = 5 # adds 5 more oranges
    total_fruits = initial_apples + initial_oranges + added_oranges

    # L2
    percentage_multiplier = 100 # WK
    percentage_apples = (initial_apples / total_fruits) * percentage_multiplier

    # FA
    answer = percentage_apples
    return answer