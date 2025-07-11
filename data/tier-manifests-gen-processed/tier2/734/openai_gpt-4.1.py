def solve():
    """Index: 734.
    Returns: the number of apples Chang's trees gave him.
    """
    # L1
    percent_total = 100 # WK (percentages sum to 100)
    percent_sweet = 75 # 75% of the apples he gets are sweet
    percent_sour = percent_total - percent_sweet

    # L2
    sweet_fraction = 0.75 # 75% of the apples he gets are sweet
    sweet_price = 0.5 # sell the sweet ones for $.5 an apple
    sour_fraction = 0.25 # rest are sour (25%)
    sour_price = 0.1 # sour ones sell for $.1 an apple
    average_price = sweet_fraction * sweet_price + sour_fraction * sour_price

    # L3
    total_earnings = 40 # he earns $40
    num_apples = total_earnings / average_price

    # FA
    answer = num_apples
    return answer