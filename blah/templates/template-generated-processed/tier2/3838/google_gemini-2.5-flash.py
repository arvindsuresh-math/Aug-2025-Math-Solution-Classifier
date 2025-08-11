def solve():
    """Index: 3838.
    Returns: the amount of change Kim gets.
    """
    # L1
    meal_cost = 10 # $10 meal
    drink_cost = 2.5 # drink for 2.5
    dinner_cost = meal_cost + drink_cost

    # L2
    tip_percent_decimal = 0.2 # 20% tip
    tip_amount = dinner_cost * tip_percent_decimal

    # L3
    total_cost = dinner_cost + tip_amount

    # L4
    bill_paid = 20 # $20 bill
    change_amount = bill_paid - total_cost

    # FA
    answer = change_amount
    return answer