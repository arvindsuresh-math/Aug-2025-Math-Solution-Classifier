def solve():
    """Index: 5669.
    Returns: the profit Jett made from selling the cow.
    """
    # L1
    days_kept = 40 # after 40 days
    food_cost_per_day = 20 # $20 every day to buy food
    total_food_cost = days_kept * food_cost_per_day

    # L2
    vaccination_deworming_cost = 500 # $500 to vaccinate and deworm the cow
    total_health_expenses = vaccination_deworming_cost + total_food_cost

    # L3
    cow_purchase_price = 600 # bought a cow from the market at $600
    total_cost_on_cow = total_health_expenses + cow_purchase_price

    # L4
    cow_selling_price = 2500 # sold the cow for $2500
    profit = cow_selling_price - total_cost_on_cow

    # FA
    answer = profit
    return answer