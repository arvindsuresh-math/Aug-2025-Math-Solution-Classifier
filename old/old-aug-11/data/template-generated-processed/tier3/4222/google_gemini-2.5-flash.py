def solve():
    """Index: 4222.
    Returns: the number of lemons in Tania's baskets.
    """
    # L1
    mangoes = 18 # 18 mangoes in one basket
    pears = 10 # 10 pears in another
    pawpaws = 12 # 12 pawpaws in another
    sum_of_first_three_baskets = mangoes + pears + pawpaws

    # L2
    total_fruits = 58 # total of 58 fruits
    fruits_in_last_two_baskets = total_fruits - sum_of_first_three_baskets

    # L3
    number_of_last_baskets = 2 # the last 2 contain the same number
    fruits_per_last_basket = fruits_in_last_two_baskets / number_of_last_baskets

    # FA
    answer = fruits_per_last_basket
    return answer