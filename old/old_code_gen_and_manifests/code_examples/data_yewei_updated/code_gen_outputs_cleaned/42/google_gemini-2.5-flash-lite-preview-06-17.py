def solve(
    num_monkeys: int = 12, # A family of 12 monkeys
    num_piles_first_type: int = 6, # 6 piles
    hands_per_pile_first_type: int = 9, # 9 hands
    bananas_per_hand_first_type: int = 14, # 14 bananas
    total_piles: int = 10, # collected 10 piles of bananas
    hands_per_pile_second_type: int = 12, # remaining piles had 12 hands
    bananas_per_hand_second_type: int = 9 # each hand having 9 bananas
):
    """Index: 42.
    Returns: the number of bananas each monkey would get if they divide the bananas equally amongst themselves.
    """
    #: L1
    bananas_first_type = num_piles_first_type * hands_per_pile_first_type * bananas_per_hand_first_type

    #: L2
    num_piles_second_type = total_piles - num_piles_first_type

    #: L3
    bananas_second_type = num_piles_second_type * hands_per_pile_second_type * bananas_per_hand_second_type

    #: L4
    total_bananas = bananas_first_type + bananas_second_type

    #: L5
    bananas_per_monkey = total_bananas / num_monkeys

    answer = bananas_per_monkey # FINAL ANSWER
    return answer