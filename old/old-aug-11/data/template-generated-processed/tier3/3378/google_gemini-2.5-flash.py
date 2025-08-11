def solve():
    """Index: 3378.
    Returns: the number of eggs each hen lays a week.
    """
    # L1
    total_sales = 120 # sold $120 worth of eggs
    price_per_dozen = 3 # sells the eggs for $3 a dozen
    total_dozen_sold = total_sales / price_per_dozen

    # L2
    num_hens = 10 # 10 hens
    dozen_per_hen_four_weeks = total_dozen_sold / num_hens

    # L3
    num_weeks = 4 # In four weeks
    dozen_per_hen_per_week = dozen_per_hen_four_weeks / num_weeks

    # L4
    eggs_per_dozen = 12 # WK
    eggs_per_hen_per_week = eggs_per_dozen * dozen_per_hen_per_week

    # FA
    answer = eggs_per_hen_per_week
    return answer