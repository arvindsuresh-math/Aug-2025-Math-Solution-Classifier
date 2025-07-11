def solve():
    """Index: 337.
    Returns: the total number of people at the gathering.
    """
    # L1
    wine_takers = 26 # 26 people took wine
    both_drinks_takers = 17 # 17 people took both drinks
    only_wine_takers = wine_takers - both_drinks_takers

    # L2
    soda_takers = 22 # 22 people took soda
    only_soda_takers = soda_takers - both_drinks_takers

    # L3
    total_people = only_wine_takers + only_soda_takers + both_drinks_takers

    # FA
    answer = total_people
    return answer