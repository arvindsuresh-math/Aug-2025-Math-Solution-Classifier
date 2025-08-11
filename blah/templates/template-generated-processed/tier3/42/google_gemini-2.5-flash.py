def solve():
    """Index: 42.
    Returns: the number of bananas each monkey would get.
    """
    # L1
    num_piles_first_type = 6 # 6 piles had 9 hands
    hands_per_pile_first_type = 9 # 9 hands
    bananas_per_hand_first_type = 14 # 14 bananas
    bananas_first_type = num_piles_first_type * hands_per_pile_first_type * bananas_per_hand_first_type

    # L2
    total_piles = 10 # 10 piles of bananas
    remaining_piles = total_piles - num_piles_first_type

    # L3
    hands_per_pile_remaining_type = 12 # remaining piles had 12 hands
    bananas_per_hand_remaining_type = 9 # each hand having 9 bananas
    bananas_remaining_type = remaining_piles * hands_per_pile_remaining_type * bananas_per_hand_remaining_type

    # L4
    total_bananas = bananas_first_type + bananas_remaining_type

    # L5
    num_monkeys = 12 # family of 12 monkeys
    bananas_per_monkey = total_bananas / num_monkeys

    # FA
    answer = bananas_per_monkey
    return answer