def solve():
    """Index: 6724.
    Returns: the total number of fruits in all baskets.
    """
    # L1
    apples_per_basket_initial = 9 # 9 apples
    oranges_per_basket_initial = 15 # 15 oranges
    apples_oranges_one_basket = apples_per_basket_initial + oranges_per_basket_initial

    # L2
    bananas_per_basket_initial = 14 # 14 bananas
    fruits_one_basket_initial = apples_oranges_one_basket + bananas_per_basket_initial

    # L3
    num_first_baskets = 3 # first three baskets
    total_fruits_first_three_baskets = num_first_baskets * fruits_one_basket_initial

    # L4
    less_fruit_fourth_basket = 2 # 2 less of each fruit in the fourth basket
    apples_fourth_basket = apples_per_basket_initial - less_fruit_fourth_basket

    # L5
    oranges_fourth_basket = oranges_per_basket_initial - less_fruit_fourth_basket

    # L6
    apples_oranges_fourth_basket = oranges_fourth_basket + apples_fourth_basket

    # L7
    bananas_fourth_basket = bananas_per_basket_initial - less_fruit_fourth_basket

    # L8
    total_fruits_fourth_basket = apples_oranges_fourth_basket + bananas_fourth_basket

    # L9
    total_fruits_all_baskets = total_fruits_fourth_basket + total_fruits_first_three_baskets

    # FA
    answer = total_fruits_all_baskets
    return answer