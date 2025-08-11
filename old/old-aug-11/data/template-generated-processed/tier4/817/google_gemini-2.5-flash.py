from fractions import Fraction

def solve():
    """Index: 817.
    Returns: the amount she spends on her coffee per week.
    """
    # L1
    cups_per_day = 2 # 2 cups of coffee per day
    ounces_per_cup = 1.5 # 1.5 ounces of coffee beans
    ounces_beans_per_day = cups_per_day * ounces_per_cup

    # L2
    days_per_week = 7 # WK
    ounces_beans_per_week = days_per_week * ounces_beans_per_day

    # L3
    ounces_per_bag = 10.5 # contains 10.5 ounces of beans
    bags_per_week = ounces_beans_per_week / ounces_per_bag

    # L4
    cost_per_bag = 8 # A bag of coffee costs $8
    cost_beans_per_week = bags_per_week * cost_per_bag

    # L5
    cost_gallon_milk = 4 # A gallon of milk costs $4
    milk_fraction_used = Fraction(1, 2) # 1/2 a gallon of milk per week
    cost_milk_per_week = cost_gallon_milk * milk_fraction_used

    # L6
    total_cost_per_week = cost_beans_per_week + cost_milk_per_week

    # FA
    answer = total_cost_per_week
    return answer