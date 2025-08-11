def solve():
    """Index: 2051.
    Returns: the number of additional apples Mary needs to buy.
    """
    # L1
    num_pies = 10 # 10 apple pies
    apples_per_pie = 8 # Each pie needs 8 apples
    total_apples_needed = num_pies * apples_per_pie

    # L2
    apples_harvested = 50 # harvested 50 apples
    apples_to_buy = total_apples_needed - apples_harvested

    # FA
    answer = apples_to_buy
    return answer