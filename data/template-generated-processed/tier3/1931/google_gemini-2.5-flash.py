def solve():
    """Index: 1931.
    Returns: the total earnings of the shop selling T-shirts per week.
    """
    # L1
    open_hours_per_day = 12 # open from 10 am until 10 pm
    minutes_per_hour = 60 # WK
    open_minutes_per_day = open_hours_per_day * minutes_per_hour

    # L2
    women_tshirt_sale_interval = 30 # women's T-shirts are sold every 30 minutes
    women_tshirts_per_day = open_minutes_per_day / women_tshirt_sale_interval

    # L3
    women_tshirt_price = 18 # for $18
    women_tshirt_earnings_per_day = women_tshirts_per_day * women_tshirt_price

    # L4
    men_tshirt_sale_interval = 40 # men's T-shirts are sold every 40 minutes
    men_tshirts_per_day = open_minutes_per_day / men_tshirt_sale_interval

    # L5
    men_tshirt_price = 15 # for $15
    men_tshirt_earnings_per_day = men_tshirts_per_day * men_tshirt_price

    # L6
    total_earnings_per_day = women_tshirt_earnings_per_day + men_tshirt_earnings_per_day

    # L7
    days_per_week = 7 # WK
    total_earnings_per_week = total_earnings_per_day * days_per_week

    # FA
    answer = total_earnings_per_week
    return answer