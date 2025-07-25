def solve():
    """Index: 734.
    Returns: the total number of apples the trees gave him.
    """
    # L1
    total_percentage = 100 # WK
    sweet_apple_percentage_num = 75 # 75% of the apples he gets are sweet
    sour_apple_percentage_num = total_percentage - sweet_apple_percentage_num

    # L2
    sweet_apple_percentage_decimal = 0.75 # 75% of the apples he gets are sweet
    sweet_apple_price = 0.5 # $.5 an apple
    sour_apple_percentage_decimal = 0.25 # the rest are sour
    sour_apple_price = 0.1 # $.1 an apple
    average_apple_price = sweet_apple_percentage_decimal * sweet_apple_price + sour_apple_percentage_decimal * sour_apple_price

    # L3
    total_earnings = 40 # If he earns $40
    total_apples = total_earnings / average_apple_price

    # FA
    answer = total_apples
    return answer