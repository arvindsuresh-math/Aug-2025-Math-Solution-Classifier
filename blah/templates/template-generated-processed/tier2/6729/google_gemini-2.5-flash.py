def solve():
    """Index: 6729.
    Returns: the total grams of sugar the company will use.
    """
    # L1
    chocolate_bars_per_minute = 36 # produces 36 chocolate bars
    sugar_per_bar = 1.5 # needs 1.5 grams of sugar
    sugar_per_minute = chocolate_bars_per_minute * sugar_per_bar

    # L2
    minutes_to_calculate = 2 # in two minutes
    total_sugar_used = sugar_per_minute * minutes_to_calculate

    # FA
    answer = total_sugar_used
    return answer