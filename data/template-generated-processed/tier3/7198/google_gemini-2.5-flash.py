def solve():
    """Index: 7198.
    Returns: the initial number of marbles Stuart had.
    """
    # L1
    betty_total_marbles = 60 # Betty had 60 marbles
    percentage_numerator = 40 # 40% of her marble collection
    percentage_denominator = 100 # WK
    marbles_given_by_betty = (percentage_numerator / percentage_denominator) * betty_total_marbles

    # L2
    stuart_final_marbles = 80 # increased to 80
    stuart_initial_marbles = stuart_final_marbles - marbles_given_by_betty

    # FA
    answer = stuart_initial_marbles
    return answer