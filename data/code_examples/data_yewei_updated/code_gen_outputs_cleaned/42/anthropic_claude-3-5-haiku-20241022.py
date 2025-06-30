def solve(
    total_piles: int = 10,  # A family of 12 monkeys collected 10 piles of bananas
    first_pile_type_count: int = 6,  # 6 piles had 9 hands
    first_pile_hands: int = 9,  # with each hand having 14 bananas
    first_pile_bananas_per_hand: int = 14,
    second_pile_hands: int = 12,  # the remaining piles had 12 hands
    second_pile_bananas_per_hand: int = 9,  # with each hand having 9 bananas
    total_monkeys: int = 12  # A family of 12 monkeys
):
    """Index: 42.
    Returns: the number of bananas each monkey would get if they divide the bananas equally.
    """
    #: L1
    first_pile_total_bananas = first_pile_type_count * first_pile_hands * first_pile_bananas_per_hand

    #: L2
    remaining_piles = total_piles - first_pile_type_count

    #: L3
    second_pile_total_bananas = remaining_piles * second_pile_hands * second_pile_bananas_per_hand

    #: L4
    total_bananas = first_pile_total_bananas + second_pile_total_bananas

    #: L5
    bananas_per_monkey = total_bananas / total_monkeys

    answer = bananas_per_monkey  # FINAL ANSWER
    return answer