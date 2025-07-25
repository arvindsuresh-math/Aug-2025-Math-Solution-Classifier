def solve():
    """Index: 6865.
    Returns: the total money Scott made.
    """
    # L1
    smoothie_price_per_cup = 3 # $3 a cup
    smoothie_cups_sold = 40 # 40 cups of smoothies
    money_from_smoothies = smoothie_price_per_cup * smoothie_cups_sold

    # L2
    cake_price_per_cake = 2 # $2 each
    cakes_sold = 18 # 18 cakes
    money_from_cakes = cake_price_per_cake * cakes_sold

    # L3
    total_money_made = money_from_smoothies + money_from_cakes

    # FA
    answer = total_money_made
    return answer