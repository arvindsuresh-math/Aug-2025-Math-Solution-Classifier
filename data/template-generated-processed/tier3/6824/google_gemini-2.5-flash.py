from fractions import Fraction

def solve():
    """Index: 6824.
    Returns: the total number of apples eaten by both girls.
    """
    # L1
    simone_fraction_per_day = Fraction(1, 2) # 1/2 of an apple each day
    simone_days = 16 # for 16 days
    simone_total_apples = simone_fraction_per_day * simone_days

    # L2
    lauri_fraction_per_day = Fraction(1, 3) # 1/3 of an apple each day
    lauri_days = 15 # for 15 days
    lauri_total_apples = lauri_fraction_per_day * lauri_days

    # L3
    total_apples_eaten = simone_total_apples + lauri_total_apples

    # FA
    answer = total_apples_eaten
    return answer