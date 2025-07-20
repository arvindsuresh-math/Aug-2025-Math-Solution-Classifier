def solve():
    """Index: 6202.
    Returns: the total number of birds on the branch to begin with.
    """
    # L1
    initial_parrots = 7 # Seven parrots
    remaining_parrots = 2 # 2 parrots left
    parrots_flew_away = initial_parrots - remaining_parrots

    # L2
    remaining_crows = 1 # 1 crow are left
    initial_crows = parrots_flew_away + remaining_crows

    # L3
    total_initial_birds = initial_parrots + initial_crows

    # FA
    answer = total_initial_birds
    return answer