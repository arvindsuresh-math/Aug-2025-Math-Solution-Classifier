def solve():
    """Index: 615.
    Returns: the year Connie's grandmother was born.
    """
    # L1
    brother_birth_year = 1932 # her grandmother's older brother was born in 1932
    sister_birth_year = 1936 # her older sister was born in 1936
    gap_brother_sister = sister_birth_year - brother_birth_year

    # L2
    gap_multiplier = 2 # gap is twice the gap between the older brother and the older sister
    gap_sister_grandma = gap_brother_sister * gap_multiplier

    # L3
    grandma_birth_year = sister_birth_year + gap_sister_grandma

    # FA
    answer = grandma_birth_year
    return answer