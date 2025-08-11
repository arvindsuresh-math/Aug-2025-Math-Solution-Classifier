def solve():
    """Index: 7036.
    Returns: the total number of dresses the three of them have.
    """
    # L1
    emily_dresses = 16 # If Emily has 16 dresses
    half_divisor = 2 # Melissa has half the number of dresses Emily has
    melissa_dresses = emily_dresses / half_divisor

    # L2
    debora_more_dresses = 12 # Debora has 12 more dresses than Melissa
    debora_dresses = melissa_dresses + debora_more_dresses

    # L3
    total_dresses = emily_dresses + melissa_dresses + debora_dresses

    # FA
    answer = total_dresses
    return answer