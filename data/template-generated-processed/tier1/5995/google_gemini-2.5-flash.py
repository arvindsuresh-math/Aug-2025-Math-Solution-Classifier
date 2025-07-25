def solve():
    """Index: 5995.
    Returns: the number of sheep Mary must buy.
    """
    # L1
    mary_sheep = 300 # Mary has 300 sheep
    bob_multiplier = 2 # double the number
    bob_extra = 35 # plus another 35
    bob_sheep = (mary_sheep * bob_multiplier) + bob_extra

    # L2
    fewer_sheep_than_bob = 69 # 69 fewer sheep than Bob
    mary_target_sheep = bob_sheep - fewer_sheep_than_bob

    # L3
    sheep_to_buy = mary_target_sheep - mary_sheep

    # FA
    answer = sheep_to_buy
    return answer