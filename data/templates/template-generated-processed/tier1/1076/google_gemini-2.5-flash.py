def solve():
    """Index: 1076.
    Returns: the total profit Stella will make.
    """
    # L1
    num_dolls = 3 # 3 dolls
    price_doll_each = 5 # $5 each
    revenue_dolls = num_dolls * price_doll_each

    # L2
    num_clocks = 2 # 2 clocks
    price_clock_each = 15 # $15 each
    revenue_clocks = num_clocks * price_clock_each

    # L3
    num_glasses = 5 # 5 glasses
    price_glass_each = 4 # $4 each
    revenue_glasses = num_glasses * price_glass_each

    # L4
    total_revenue = revenue_dolls + revenue_clocks + revenue_glasses

    # L5
    total_cost = 40 # $40 to buy everything
    total_profit = total_revenue - total_cost

    # FA
    answer = total_profit
    return answer