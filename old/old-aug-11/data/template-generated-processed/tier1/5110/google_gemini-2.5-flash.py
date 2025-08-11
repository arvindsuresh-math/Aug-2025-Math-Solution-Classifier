def solve():
    """Index: 5110.
    Returns: the number of Butterfingers Mark has.
    """
    # L1
    snickers = 3 # 3 Snickers
    mars_bars = 2 # 2 Mars bars
    other_candy_bars = snickers + mars_bars

    # L2
    total_candy_bars = 12 # 12 candy bars in total
    butterfingers = total_candy_bars - other_candy_bars

    # FA
    answer = butterfingers
    return answer