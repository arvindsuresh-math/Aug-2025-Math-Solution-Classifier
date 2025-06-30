def solve():
    # Number of monkeys
    num_monkeys = 12

    # Information for the first type of piles
    num_piles_type1 = 6
    hands_per_pile_type1 = 9
    bananas_per_hand_type1 = 14

    # Calculate bananas from the first type of piles
    # L1: The first 6 bunches had 6 x 9 x 14 = 756 bananas.
    bananas_type1 = num_piles_type1 * hands_per_pile_type1 * bananas_per_hand_type1

    # Total number of piles
    total_piles = 10

    # Information for the remaining piles (second type)
    # L2: There were 10 - 6 = 4 remaining bunches.
    num_piles_type2 = total_piles - num_piles_type1
    hands_per_pile_type2 = 12
    bananas_per_hand_type2 = 9

    # Calculate bananas from the remaining piles
    # L3: The 4 remaining bunches had 4 x 12 x 9 = 432 bananas.
    bananas_type2 = num_piles_type2 * hands_per_pile_type2 * bananas_per_hand_type2

    # Calculate the total number of bananas
    # L4: All together, there were 756 + 432 = 1188 bananas
    total_bananas = bananas_type1 + bananas_type2

    # Calculate how many bananas each monkey gets
    # L5: Each monkey would get 1188/12 = 99 bananas.
    bananas_per_monkey = total_bananas / num_monkeys

    return {
        "L1": f"The first {num_piles_type1} bunches had {num_piles_type1} x {hands_per_pile_type1} x {bananas_per_hand_type1} = [[{bananas_type1}]] bananas.",
        "L2": f"There were {total_piles} - {num_piles_type1} = [[{num_piles_type2}]] remaining bunches.",
        "L3": f"The {num_piles_type2} remaining bunches had {num_piles_type2} x {hands_per_pile_type2} x {bananas_per_hand_type2} = [[{bananas_type2}]] bananas.",
        "L4": f"All together, there were {bananas_type1} + {bananas_type2} = [[{total_bananas}]] bananas",
        "L5": f"Each monkey would get {total_bananas}/{num_monkeys} = [[{int(bananas_per_monkey)}]] bananas."
    }