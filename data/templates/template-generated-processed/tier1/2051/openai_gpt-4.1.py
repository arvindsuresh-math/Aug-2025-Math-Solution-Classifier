def solve():
    """Index: 2051.
    Returns: the number of apples Mary needs to buy to make all 10 pies.
    """
    # L1
    num_pies = 10 # bake 10 apple pies
    apples_per_pie = 8 # Each pie needs 8 apples
    total_apples_needed = num_pies * apples_per_pie

    # L2
    apples_harvested = 50 # she already harvested 50 apples
    apples_to_buy = total_apples_needed - apples_harvested

    # FA
    answer = apples_to_buy
    return answer