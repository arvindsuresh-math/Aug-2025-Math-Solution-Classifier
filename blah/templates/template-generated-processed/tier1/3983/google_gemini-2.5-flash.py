def solve():
    """Index: 3983.
    Returns: the total number of eggs needed for the dinner party.
    """
    # L1
    eggs_per_savory_souffle = 8 # 8 eggs each
    num_savory_souffles = 3 # make 3 savory soufflés
    eggs_for_savory = eggs_per_savory_souffle * num_savory_souffles

    # L2
    eggs_per_dessert_souffle = 6 # 6 eggs each
    num_dessert_souffles = 5 # make 5 dessert soufflés
    eggs_for_dessert = eggs_per_dessert_souffle * num_dessert_souffles

    # L3
    total_eggs_needed = eggs_for_savory + eggs_for_dessert

    # FA
    answer = total_eggs_needed
    return answer