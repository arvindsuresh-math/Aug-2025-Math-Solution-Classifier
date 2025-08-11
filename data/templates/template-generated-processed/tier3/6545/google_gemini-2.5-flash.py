def solve():
    """Index: 6545.
    Returns: the number of days until the coffee machine pays for itself.
    """
    # L1
    machine_cost_initial = 200 # coffee machine for $200
    discount = 20 # gets a $20 discount
    machine_cost_after_discount = machine_cost_initial - discount

    # L2
    cost_per_coffee = 4 # $4 each
    coffees_per_day = 2 # 2 coffees a day
    daily_old_spending = cost_per_coffee * coffees_per_day

    # L3
    daily_new_cost = 3 # $3 a day to make his coffee
    daily_savings = daily_old_spending - daily_new_cost

    # L4
    days_to_pay_off = machine_cost_after_discount / daily_savings

    # FA
    answer = days_to_pay_off
    return answer