def solve():
    """Index: 6924.
    Returns: the number of male contestants.
    """
    # L1
    total_contestants = 18 # 18 contestants in total
    female_fraction_denominator = 3 # A third of the contestants
    female_contestants = total_contestants / female_fraction_denominator

    # L2
    male_contestants = total_contestants - female_contestants

    # FA
    answer = male_contestants
    return answer