def solve():
    """Index: 2198.
    Returns: the number of pairs of socks Jonas needs to buy.
    """
    # L1
    initial_sock_pairs = 20 # 20 pairs of socks
    items_per_pair = 2 # two items each
    initial_individual_socks = initial_sock_pairs * items_per_pair

    # L2
    initial_shoe_pairs = 5 # 5 pairs of shoes
    initial_individual_shoes = initial_shoe_pairs * items_per_pair

    # L3
    initial_pants = 10 # 10 pairs of pants
    initial_tshirts = 10 # 10 t-shirts
    total_initial_items = initial_individual_socks + initial_individual_shoes + initial_pants + initial_tshirts

    # L4
    double_factor = 2 # double the number
    target_total_items = total_initial_items * double_factor

    # L5
    new_items_needed = target_total_items - total_initial_items

    # L6
    new_sock_pairs_needed = new_items_needed / items_per_pair

    # FA
    answer = new_sock_pairs_needed
    return answer