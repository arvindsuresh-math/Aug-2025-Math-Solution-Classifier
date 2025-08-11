def solve():
    """Index: 3228.
    Returns: how much more money Daisy spent on lunch than on breakfast.
    """
    # L1
    muffin_cost = 2 # muffin for $2
    coffee_cost = 4 # cup of coffee for $4
    breakfast_total_cost = muffin_cost + coffee_cost

    # L2
    soup_cost = 3 # soup cost $3
    salad_cost = 5.25 # salad cost $5.25
    lemonade_cost = 0.75 # lemonade cost $0.75
    lunch_total_cost = soup_cost + salad_cost + lemonade_cost

    # L3
    difference_in_cost = lunch_total_cost - breakfast_total_cost

    # FA
    answer = difference_in_cost
    return answer