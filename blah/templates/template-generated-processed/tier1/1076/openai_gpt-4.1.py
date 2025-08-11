def solve():
    """Index: 1076.
    Returns: the total profit Stella will make after selling all merchandise.
    """
    # L1
    num_dolls = 3 # 3 dolls
    price_per_doll = 5 # $5 each
    dolls_revenue = num_dolls * price_per_doll

    # L2
    num_clocks = 2 # 2 clocks
    price_per_clock = 15 # $15 each
    clocks_revenue = num_clocks * price_per_clock

    # L3
    num_glasses = 5 # 5 glasses
    price_per_glass = 4 # $4 each
    glasses_revenue = num_glasses * price_per_glass

    # L4
    total_revenue = dolls_revenue + clocks_revenue + glasses_revenue

    # L5
    total_cost = 40 # spent $40 to buy everything
    profit = total_revenue - total_cost

    # FA
    answer = profit
    return answer