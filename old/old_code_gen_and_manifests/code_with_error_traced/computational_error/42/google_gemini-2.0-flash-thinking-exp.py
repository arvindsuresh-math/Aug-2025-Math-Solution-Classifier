def solve(
    num_monkeys: int = 12, # A family of 12 monkeys
    total_piles: int = 10, # collected 10 piles of bananas
    num_piles_type1: int = 6, # 6 piles
    hands_per_pile_type1: int = 9, # had 9 hands
    bananas_per_hand_type1: int = 14, # with each hand having 14 bananas
    hands_per_pile_type2: int = 12, # the remaining piles had 12 hands
    bananas_per_hand_type2: int = 9 # with each hand having 9 bananas
):
    """Index: 42.
    Returns: the number of bananas each monkey would get if divided equally.
    """

    #: L1
    bananas_type1_piles = num_piles_type1 * hands_per_pile_type1 * bananas_per_hand_type1 # eval: 756 = 6 * 9 * 14

    #: L2
    num_piles_type2 = total_piles - num_piles_type1 # eval: 4 = 10 - 6

    #: L3
    bananas_type2_piles = num_piles_type2 * hands_per_pile_type2 * bananas_per_hand_type2 # eval: 432 = 4 * 12 * 9

    #: L4
    total_bananas = bananas_type1_piles + bananas_type2_piles # eval: 1188 = 756 + 432

    #: L5
    bananas_per_monkey = 89.0 # eval: 89.0 = 89.0

    #: FA
    answer = bananas_per_monkey
    return answer # eval: return 89.0
