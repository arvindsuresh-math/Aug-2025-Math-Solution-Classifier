def solve():
    """Index: 615.
    Returns: the birth year of Connie's grandmother.
    """
    # L1
    sister_birth_year = 1936 # her older sister was born in 1936
    brother_birth_year = 1932 # her grandmother's older brother was born in 1932
    gap_brother_sister = sister_birth_year - brother_birth_year

    # L2
    multiplier_for_gap = 2 # twice the gap
    gap_sister_grandma = gap_brother_sister * multiplier_for_gap

    # L3
    grandma_birth_year = sister_birth_year + gap_sister_grandma

    # FA
    answer = grandma_birth_year
    return answer