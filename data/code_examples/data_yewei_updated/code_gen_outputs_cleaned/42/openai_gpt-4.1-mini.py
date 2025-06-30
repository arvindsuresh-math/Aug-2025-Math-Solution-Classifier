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
    bananas_in_6_piles = piles_with_9_hands * 9 * bananas_per_hand_9hands

    #: L2
    remaining_piles = total_piles - piles_with_9_hands

    #: L3
    bananas_in_remaining_piles = remaining_piles * hands_in_remaining_piles * bananas_per_hand_12hands

    #: L4
    total_bananas = bananas_in_6_piles + bananas_in_remaining_piles

    #: L5
    bananas_per_monkey = total_bananas / num_monkeys

    answer = bananas_per_monkey  # FINAL ANSWER
    return answer