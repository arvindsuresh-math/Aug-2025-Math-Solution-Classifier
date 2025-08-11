def solve():
    """Index: 4211.
    Returns: the number of bananas in basket E.
    """
    # L1
    average_fruits_per_basket = 25 # The average number of fruits per basket in five baskets is 25
    num_baskets = 5 # five baskets
    total_fruits = average_fruits_per_basket * num_baskets

    # L2
    apples = 15 # basket A contains 15 apples
    mangoes = 30 # B has 30 mangoes
    peaches = 20 # C has 20 peaches
    pears = 25 # D has 25 pears
    sum_other_fruits = apples + mangoes + peaches + pears

    # L3
    bananas_in_basket_e = total_fruits - sum_other_fruits

    # FA
    answer = bananas_in_basket_e
    return answer