def solve(
    total_piles: int = 10,  # 10 piles of bananas
    first_pile_type_count: int = 6,  # 6 piles had 9 hands
    first_pile_hands: int = 9,  # each of these piles had 9 hands
    first_pile_bananas_per_hand: int = 14,  # each hand had 14 bananas
    second_pile_hands: int = 12,  # remaining piles had 12 hands
    second_pile_bananas_per_hand: int = 9,  # each hand had 9 bananas
    total_monkeys: int = 12  # a family of 12 monkeys
):
    """Index: 42.
    Returns: the number of bananas each monkey would get if bananas are divided equally.
    """

    #: L1
    first_pile_total_bananas = first_pile_type_count * first_pile_hands * first_pile_bananas_per_hand # eval: 756 = 6 * 9 * 14

    #: L2
    second_pile_type_count = first_pile_hands - first_pile_type_count # eval: 3 = 9 - 6

    #: L3
    second_pile_total_bananas = second_pile_type_count * second_pile_hands * second_pile_bananas_per_hand # eval: 324 = 3 * 12 * 9

    #: L4
    total_bananas = first_pile_total_bananas + second_pile_total_bananas # eval: 1080 = 756 + 324

    #: L5
    bananas_per_monkey = total_bananas / total_monkeys # eval: 90.0 = 1080 / 12

    #: FA
    answer = bananas_per_monkey
    return answer # eval: return 90.0
