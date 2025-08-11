def solve():
    """Index: 6948.
    Returns: the number of cherry saplings Kim has left.
    """
    # L1
    cherry_pits_planted = 80 # plants 80 cherry pits
    sprout_percentage_num = 25 # 25% of them sprout
    percent_to_decimal_factor = 0.01 # WK
    sprouted_saplings = cherry_pits_planted * sprout_percentage_num * percent_to_decimal_factor

    # L2
    saplings_sold = 6 # sells 6 of the saplings
    saplings_left = sprouted_saplings - saplings_sold

    # FA
    answer = saplings_left
    return answer