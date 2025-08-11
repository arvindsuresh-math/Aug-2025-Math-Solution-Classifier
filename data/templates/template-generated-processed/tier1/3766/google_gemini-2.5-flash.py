def solve():
    """Index: 3766.
    Returns: the total number of blueberries Miss Darlington had.
    """
    # L1
    num_additional_baskets = 9 # picked 9 more baskets
    blueberries_in_each_additional_basket = 20 # same amount of berries (as the initial 20)
    blueberries_from_additional_baskets = num_additional_baskets * blueberries_in_each_additional_basket

    # L2
    initial_blueberries = 20 # a basket of 20 blueberries
    total_blueberries = blueberries_from_additional_baskets + initial_blueberries

    # FA
    answer = total_blueberries
    return answer