def solve():
    """Index: 7455.
    Returns: the total profit the shop made in one month.
    """
    # L1
    tire_repair_charge = 20 # charges $20 for this
    tire_repair_cost = 5 # cost him $5 in parts
    profit_per_tire_repair = tire_repair_charge - tire_repair_cost

    # L2
    num_tire_repairs = 300 # Jim does 300 of these repairs
    total_profit_tire_repairs = profit_per_tire_repair * num_tire_repairs

    # L3
    complex_repair_charge = 300 # for $300 each
    complex_repair_cost = 50 # cost $50 in parts
    profit_per_complex_repair = complex_repair_charge - complex_repair_cost

    # L4
    num_complex_repairs = 2 # 2 more complex repairs
    total_profit_complex_repairs = profit_per_complex_repair * num_complex_repairs

    # L5
    retail_profit = 2000 # sells $2000 profit worth of things from his retail shop
    gross_profit = total_profit_tire_repairs + total_profit_complex_repairs + retail_profit

    # L6
    fixed_expenses = 4000 # rent and other fixed expense for the shop is $4000 a month
    net_profit = gross_profit - fixed_expenses

    # FA
    answer = net_profit
    return answer