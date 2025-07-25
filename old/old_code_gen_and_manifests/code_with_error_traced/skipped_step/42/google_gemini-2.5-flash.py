def solve(
        num_monkeys: int = 12, # A family of 12 monkeys
        total_piles: int = 10, # collected 10 piles of bananas
        piles_type1: int = 6, # 6 piles
        hands_per_pile_type1: int = 9, # had 9 hands
        bananas_per_hand_type1: int = 14, # with each hand having 14 bananas
        hands_per_pile_type2: int = 12, # the remaining piles had 12 hands
        bananas_per_hand_type2: int = 9 # with each hand having 9 bananas
    ):
    """Index: 42.
    Returns: the number of bananas each monkey would get if divided equally.
    """

    #: L1
    bananas_from_type1_piles = piles_type1 * hands_per_pile_type1 * bananas_per_hand_type1 # eval: 756 = 6 * 9 * 14

    #: L2

    #: L3
    bananas_from_type2_piles = bananas_per_hand_type1 * hands_per_pile_type2 * bananas_per_hand_type2 # eval: 1512 = 14 * 12 * 9

    #: L4
    total_bananas = bananas_from_type1_piles + bananas_from_type2_piles # eval: 2268 = 756 + 1512

    #: L5
    bananas_per_monkey = total_bananas / num_monkeys # eval: 189.0 = 2268 / 12

    #: FA
    answer = bananas_per_monkey
    return answer # eval: return 189.0
