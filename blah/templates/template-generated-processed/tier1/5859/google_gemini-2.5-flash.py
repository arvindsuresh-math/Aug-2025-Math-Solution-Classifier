def solve():
    """Index: 5859.
    Returns: the total grams of sugar in all the candy bought.
    """
    # L1
    chocolate_bars_count = 14 # 14 chocolate bars
    sugar_per_bar = 10 # 10 grams of sugar
    total_sugar_chocolate_bars = chocolate_bars_count * sugar_per_bar

    # L2
    sugar_lollipop = 37 # an additional 37 grams of sugar
    total_sugar_all_candy = total_sugar_chocolate_bars + sugar_lollipop

    # FA
    answer = total_sugar_all_candy
    return answer