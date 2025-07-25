def solve():
    """Index: 1929.
    Returns: the total number of beanie babies Lori and Sydney have.
    """
    # L1
    lori_beanie_babies = 300 # Lori has 300 beanie babies
    lori_sydney_ratio = 15 # 15 times as many beanie babies as Sydney
    sydney_beanie_babies = lori_beanie_babies / lori_sydney_ratio

    # L2
    total_beanie_babies = sydney_beanie_babies + lori_beanie_babies

    # FA
    answer = total_beanie_babies
    return answer