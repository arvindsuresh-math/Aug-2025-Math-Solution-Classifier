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

    #: L2
    second_pile_type_count = total_piles - first_pile_type_count

    #: L3
    second_pile_total_bananas = second_pile_type_count * second_pile_hands * second_pile_bananas_per_hand

    #: L4
    total_bananas = total_piles + second_pile_total_bananas

    #: L5
    bananas_per_monkey = total_bananas / total_monkeys

    #: FA
    answer = bananas_per_monkey
    return answer