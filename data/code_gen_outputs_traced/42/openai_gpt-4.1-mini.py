def solve(
    num_monkeys: int = 12,  # A family of 12 monkeys
    total_piles: int = 10,  # collected 10 piles of bananas
    piles_with_9_hands: int = 6,  # 6 piles had 9 hands
    bananas_per_hand_9hands: int = 14,  # each hand having 14 bananas
    hands_in_remaining_piles: int = 12,  # remaining piles had 12 hands
    bananas_per_hand_12hands: int = 9  # each hand having 9 bananas
):
    """Index: 42.
    Returns: the number of bananas each monkey gets if divided equally.
    """

    #: L1
    bananas_in_6_piles = piles_with_9_hands * 9 * bananas_per_hand_9hands # eval: 756 = 6 * 9 * 14

    #: L2
    remaining_piles = total_piles - piles_with_9_hands # eval: 4 = 10 - 6

    #: L3
    bananas_in_remaining_piles = remaining_piles * hands_in_remaining_piles * bananas_per_hand_12hands # eval: 432 = 4 * 12 * 9

    #: L4
    total_bananas = bananas_in_6_piles + bananas_in_remaining_piles # eval: 1188 = 756 + 432

    #: L5
    bananas_per_monkey = total_bananas / num_monkeys # eval: 99.0 = 1188 / 12

    #: FA
    answer = bananas_per_monkey
    return answer # eval: return 99.0
