def solve():
    """Index: 1092.
    Returns: the total number of polka-dot blankets Estevan has.
    """
    # L1
    total_blankets = 24 # Estevan has 24 blankets
    polka_dot_divisor = 3 # One-third of the blankets
    initial_polka_dot_blankets = total_blankets / polka_dot_divisor

    # L2
    new_polka_dot_blankets = 2 # 2 more polka-dot print blankets
    total_polka_dot_blankets = initial_polka_dot_blankets + new_polka_dot_blankets

    # FA
    answer = total_polka_dot_blankets
    return answer