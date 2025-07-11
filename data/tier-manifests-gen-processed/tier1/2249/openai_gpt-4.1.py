def solve():
    """Index: 2249.
    Returns: the additional money made in a day during high season compared to low season.
    """
    # L1
    high_season_packs_per_hour = 6 # 6 packs of tuna fish are sold per hour
    hours_sold = 15 # fish are sold for 15 hours
    high_season_total_packs = high_season_packs_per_hour * hours_sold

    # L2
    price_per_pack = 60 # $60 per pack
    high_season_total_sales = high_season_total_packs * price_per_pack

    # L3
    low_season_packs_per_hour = 4 # 4 tuna packs are sold per hour
    low_season_total_packs = low_season_packs_per_hour * hours_sold

    # L4
    low_season_total_sales = low_season_total_packs * price_per_pack

    # L5
    additional_money = high_season_total_sales - low_season_total_sales

    # FA
    answer = additional_money
    return answer