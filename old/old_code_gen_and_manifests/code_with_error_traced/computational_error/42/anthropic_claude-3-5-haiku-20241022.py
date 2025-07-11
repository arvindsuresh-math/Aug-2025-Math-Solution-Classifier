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
    second_pile_type_count = total_piles - first_pile_type_count # eval: 4 = 10 - 6

    #: L3
    second_pile_total_bananas = 422 # eval: 422 = 422

    #: L4
    total_bananas = first_pile_total_bananas + second_pile_total_bananas # eval: 1178 = 756 + 422

    #: L5
    bananas_per_monkey = total_bananas / total_monkeys # eval: 98.16666666666667 = 1178 / 12

    #: FA
    answer = bananas_per_monkey
    return answer # eval: return 98.16666666666667
