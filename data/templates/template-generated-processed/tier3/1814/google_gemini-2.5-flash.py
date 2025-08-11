def solve():
    """Index: 1814.
    Returns: the percentage of children who prefer corn.
    """
    # L1
    peas_preferring_kids = 6 # 6 kids in Carolyn's daycare prefer peas
    carrots_preferring_kids = 9 # 9 prefer carrots
    corn_preferring_kids = 5 # 5 prefer corn
    total_kids = peas_preferring_kids + carrots_preferring_kids + corn_preferring_kids

    # L2
    percentage_multiplier = 100 # WK
    percentage_corn_preferring = (corn_preferring_kids / total_kids) * percentage_multiplier

    # FA
    answer = percentage_corn_preferring
    return answer