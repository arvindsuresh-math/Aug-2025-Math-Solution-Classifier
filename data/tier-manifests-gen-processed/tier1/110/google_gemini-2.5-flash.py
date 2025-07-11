def solve():
    """Index: 110.
    Returns: how much more money Tina made compared to Marvin.
    """
    # L1
    marvin_candy_bars_sold = 35 # Marvin sold 35 candy bars total
    candy_bar_cost = 2 # The candy bars cost $2 each
    marvin_money_made = marvin_candy_bars_sold * candy_bar_cost

    # L2
    tina_multiplier = 3 # Tina sold three times the number of candy bars as Marvin
    tina_money_made = marvin_money_made * tina_multiplier

    # L3
    money_difference = tina_money_made - marvin_money_made

    # FA
    answer = money_difference
    return answer