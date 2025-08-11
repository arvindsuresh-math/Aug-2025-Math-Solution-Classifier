def solve():
    """Index: 2804.
    Returns: the total number of tears Trent cries.
    """
    # L1
    onions_per_pot = 4 # 4 onions per pot
    num_pots = 6 # 6 pots of soup
    total_onions = onions_per_pot * num_pots

    # L2
    onions_per_set_of_tears = 3 # three onions per 2 tears
    num_sets_of_tears = total_onions / onions_per_set_of_tears

    # L3
    tears_per_set = 2 # 2 tears for every three onions
    total_tears = num_sets_of_tears * tears_per_set

    # FA
    answer = total_tears
    return answer