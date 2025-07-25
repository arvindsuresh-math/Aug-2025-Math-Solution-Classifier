def solve():
    """Index: 337.
    Returns: the total number of people at the gathering.
    """
    # L1
    wine = 26 # 26 people took wine
    both = 17 # 17 people took both drinks
    wine_only = wine - both

    # L2
    soda = 22 # 22 people took soda
    soda_only = soda - both

    # L3
    total_people = wine_only + soda_only + both

    # FA
    answer = total_people
    return answer