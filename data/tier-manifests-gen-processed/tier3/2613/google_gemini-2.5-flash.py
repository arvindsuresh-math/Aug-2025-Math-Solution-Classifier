def solve():
    """Index: 2613.
    Returns: the number of pounds of cheese Tony bought.
    """
    # L1
    initial_money = 87 # Tony has $87
    money_left = 61 # he has $61 left
    money_spent = initial_money - money_left

    # L2
    beef_cost_per_pound = 5 # a pound of beef that costs $5 a pound
    money_spent_on_cheese = money_spent - beef_cost_per_pound

    # L3
    cheese_cost_per_pound = 7 # cheese, which costs $7 a pound
    pounds_of_cheese = money_spent_on_cheese / cheese_cost_per_pound

    # FA
    answer = pounds_of_cheese
    return answer