def solve():
    """Index: 439.
    Returns: the total number of key chain pieces Timothy can buy.
    """
    # L1
    tshirt_cost_per_piece = 8 # t-shirts that cost $8 each
    num_tshirts = 2 # buys 2 t-shirts
    cost_tshirts = tshirt_cost_per_piece * num_tshirts

    # L2
    bag_cost_per_piece = 10 # bags that cost $10 each
    num_bags = 2 # and 2 bags
    cost_bags = bag_cost_per_piece * num_bags

    # L3
    total_spent_shirts_bags = cost_tshirts + cost_bags

    # L4
    initial_money = 50 # Timothy has $50 to spend
    money_left = initial_money - total_spent_shirts_bags

    # L5
    keychain_set_cost = 2 # key chains that sell 3 pieces for $2
    num_keychain_sets = money_left / keychain_set_cost

    # L6
    pieces_per_keychain_set = 3 # key chains that sell 3 pieces for $2
    total_keychain_pieces = num_keychain_sets * pieces_per_keychain_set

    # FA
    answer = total_keychain_pieces
    return answer