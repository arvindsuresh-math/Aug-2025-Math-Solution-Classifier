def solve():
    """Index: 5114.
    Returns: the number of Snickers bars Jaron needs to sell.
    """
    # L1
    chocolate_bunnies_sold = 8 # sold 8 chocolate bunnies
    points_per_bunny = 100 # worth 100 points each
    points_from_bunnies = chocolate_bunnies_sold * points_per_bunny

    # L2
    points_needed_for_switch = 2000 # needs 2000 points for the Nintendo Switch
    remaining_points_needed = points_needed_for_switch - points_from_bunnies

    # L3
    points_per_snickers = 25 # Each Snickers bar he sells earns 25 points
    snickers_bars_to_sell = remaining_points_needed / points_per_snickers

    # FA
    answer = snickers_bars_to_sell
    return answer