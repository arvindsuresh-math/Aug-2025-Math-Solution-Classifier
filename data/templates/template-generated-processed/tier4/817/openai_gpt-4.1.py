def solve():
    """Index: 817.
    Returns: the total amount Maddie's mom spends on coffee per week.
    """
    # L1
    cups_per_day = 2 # makes herself 2 cups of coffee per day
    beans_per_cup = 1.5 # each cup has 1.5 ounces of coffee beans
    beans_per_day = cups_per_day * beans_per_cup

    # L2
    days_per_week = 7 # WK
    beans_per_week = days_per_week * beans_per_day

    # L3
    ounces_per_bag = 10.5 # a bag of coffee contains 10.5 ounces of beans
    bags_per_week = beans_per_week / ounces_per_bag

    # L4
    cost_per_bag = 8 # a bag of coffee costs $8
    beans_cost_per_week = bags_per_week * cost_per_bag

    # L5
    milk_per_week = 0.5 # uses 1/2 a gallon of milk per week
    cost_per_gallon_milk = 4 # a gallon of milk costs $4
    milk_cost_per_week = cost_per_gallon_milk * milk_per_week

    # L6
    total_cost_per_week = beans_cost_per_week + milk_cost_per_week

    # FA
    answer = total_cost_per_week
    return answer