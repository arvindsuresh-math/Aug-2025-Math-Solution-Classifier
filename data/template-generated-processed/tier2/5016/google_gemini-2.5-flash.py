def solve():
    """Index: 5016.
    Returns: the average number of marbles of other colors the friend will get.
    """
    # L1
    total_percentage = 100 # WK
    black_percent = 20 # 20% are black
    clear_percent = 40 # 40% of them are clear
    other_colors_percent = total_percentage - black_percent - clear_percent

    # L2
    marbles_taken = 5 # take five marbles
    other_colors_decimal = 0.4 # 40% as a decimal, derived from the remainder of colors
    average_other_colors_marbles = marbles_taken * other_colors_decimal

    # FA
    answer = average_other_colors_marbles
    return answer