def solve():
    """Index: 439.
    Returns: the number of key chain pieces Timothy can buy with his remaining money.
    """
    # L1
    tshirt_price = 8 # t-shirts that cost $8 each
    tshirt_quantity = 2 # buys 2 t-shirts
    tshirt_total = tshirt_price * tshirt_quantity

    # L2
    bag_price = 10 # bags that cost $10 each
    bag_quantity = 2 # buys 2 bags
    bag_total = bag_price * bag_quantity

    # L3
    spent = tshirt_total + bag_total

    # L4
    initial_money = 50 # Timothy has $50
    remaining_money = initial_money - spent

    # L5
    keychain_set_price = 2 # key chains that sell 3 pieces for $2
    keychain_sets = remaining_money / keychain_set_price

    # L6
    keychains_per_set = 3 # 3 pieces per set # WK
    keychain_pieces = keychain_sets * keychains_per_set

    # FA
    answer = keychain_pieces
    return answer