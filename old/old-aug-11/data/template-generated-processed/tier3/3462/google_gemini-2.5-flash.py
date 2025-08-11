def solve():
    """Index: 3462.
    Returns: the number of cats remaining on the island.
    """
    # L1
    original_cats = 1800 # number of cats originally on the island was 1800
    first_relocation_amount = 600 # 600 cats were relocated
    cats_after_first_mission = original_cats - first_relocation_amount

    # L2
    second_relocation_divisor = 2 # half of the remaining cats
    cats_second_mission = cats_after_first_mission / second_relocation_divisor

    # L3
    remaining_cats = cats_after_first_mission - cats_second_mission

    # FA
    answer = remaining_cats
    return answer