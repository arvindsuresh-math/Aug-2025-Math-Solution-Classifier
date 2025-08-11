def solve():
    """Index: 110.
    Returns: how much more money Tina made for the class trip than Marvin by selling candy bars.
    """
    # L1
    marvin_bars = 35 # Marvin sold 35 candy bars total
    price_per_bar = 2 # The candy bars cost $2 each
    marvin_money = marvin_bars * price_per_bar

    # L2
    tina_times_marvin = 3 # Tina sold three times the number of candy bars as Marvin
    tina_money = marvin_money * tina_times_marvin

    # L3
    difference = tina_money - marvin_money

    # FA
    answer = difference
    return answer