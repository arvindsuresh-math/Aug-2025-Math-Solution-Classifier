def solve():
    """Index: 5829.
    Returns: the money made per minute during the sale.
    """
    # L1
    total_shirts_sold = 200 # 200 t-shirts
    half_divisor = 2 # Half of the shirts
    black_shirts_count = total_shirts_sold / half_divisor # half of the shirts were black
    black_shirt_cost = 30 # cost $30
    revenue_black_shirts = black_shirts_count * black_shirt_cost

    # L2
    white_shirts_count = total_shirts_sold / half_divisor # the other half were white
    white_shirt_cost = 25 # cost $25
    revenue_white_shirts = white_shirts_count * white_shirt_cost

    # L3
    total_revenue = revenue_black_shirts + revenue_white_shirts

    # L4
    sale_duration_minutes = 25 # in 25 minutes
    money_per_minute = total_revenue / sale_duration_minutes

    # FA
    answer = money_per_minute
    return answer