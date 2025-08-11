def solve():
    """Index: 3368.
    Returns: the total number of strawberries picked by Lilibeth and her friends.
    """
    # L1
    lilibeth_baskets = 6 # Lilibeth fills 6 baskets
    strawberries_per_basket = 50 # each basket holds 50 strawberries
    lilibeth_total_strawberries = lilibeth_baskets * strawberries_per_basket

    # L2
    lilibeth_count = 1 # WK
    num_friends = 3 # three of Lilibeth's friends
    total_pickers = lilibeth_count + num_friends

    # L3
    total_strawberries_picked = lilibeth_total_strawberries * total_pickers

    # FA
    answer = total_strawberries_picked
    return answer