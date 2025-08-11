def solve():
    """Index: 1459.
    Returns: the total amount James spends on coffee in a week.
    """
    # L1
    other_people = 3 # 3 other people in the house
    james = 1 # James himself
    total_people = other_people + james

    # L2
    cups_per_person_per_day = 2 # everyone drinks 2 cups of coffee a day
    total_cups_per_day = total_people * cups_per_person_per_day

    # L3
    ounces_per_cup = 0.5 # .5 ounces of coffee per cup
    total_ounces_per_day = total_cups_per_day * ounces_per_cup

    # L4
    days_per_week = 7 # WK
    total_ounces_per_week = total_ounces_per_day * days_per_week

    # L5
    cost_per_ounce = 1.25 # coffee costs $1.25 an ounce
    total_cost = total_ounces_per_week * cost_per_ounce

    # FA
    answer = total_cost
    return answer