def solve():
    """Index: 42.
    Returns: the number of bananas each monkey would get if divided equally.
    """
    # L1
    first_bunches = 6 # 6 piles had 9 hands
    hands_per_first_bunch = 9 # 6 piles had 9 hands
    bananas_per_hand_first = 14 # each hand having 14 bananas
    bananas_first_bunches = first_bunches * hands_per_first_bunch * bananas_per_hand_first

    # L2
    total_bunches = 10 # 10 piles of bananas
    remaining_bunches = total_bunches - first_bunches

    # L3
    hands_per_remaining_bunch = 12 # remaining piles had 12 hands
    bananas_per_hand_remaining = 9 # each hand having 9 bananas
    bananas_remaining_bunches = remaining_bunches * hands_per_remaining_bunch * bananas_per_hand_remaining

    # L4
    total_bananas = bananas_first_bunches + bananas_remaining_bunches

    # L5
    monkeys = 12 # family of 12 monkeys
    bananas_per_monkey = total_bananas / monkeys

    # FA
    answer = bananas_per_monkey
    return answer