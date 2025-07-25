def solve():
    """Index: 3788.
    Returns: the total number of sharks counted over two days.
    """
    # L1
    fish_day1 = 15 # On day one she counts 15 fish
    multiplier_day2 = 3 # three times as many
    fish_day2 = multiplier_day2 * fish_day1

    # L2
    total_fish = fish_day1 + fish_day2

    # L3
    shark_percentage_decimal = 0.25 # 25% will be sharks
    total_sharks = total_fish * shark_percentage_decimal

    # FA
    answer = total_sharks
    return answer