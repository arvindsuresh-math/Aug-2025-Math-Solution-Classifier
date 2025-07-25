def solve():
    """Index: 2378.
    Returns: the total amount Tony paid for all toys.
    """
    # L1
    num_lego = 3 # bought 3 sets of lego
    price_lego = 250 # $250 a set of Lego blocks
    total_lego = num_lego * price_lego

    # L2
    num_sword = 7 # 7 toy swords
    price_sword = 120 # $120 worth toy sword
    total_sword = num_sword * price_sword

    # L3
    num_dough = 10 # 10 play doughs
    price_dough = 35 # $35 play dough
    total_dough = num_dough * price_dough

    # L4
    total_cost = total_lego + total_sword + total_dough

    # FA
    answer = total_cost
    return answer