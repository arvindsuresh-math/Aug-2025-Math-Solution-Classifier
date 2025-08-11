def solve():
    """Index: 4880.
    Returns: how much money Jim's cousin brought.
    """
    # L1
    cheeseburger_cost = 3 # A cheeseburger is $3
    milkshake_cost = 5 # A milkshake is $5
    cost_per_person_items = cheeseburger_cost + milkshake_cost

    # L2
    num_people = 2 # Jim and his Cousin
    total_cost_individual_items = num_people * cost_per_person_items

    # L3
    cheese_fries_cost = 8 # Cheese fries are $8
    total_meal_cost = total_cost_individual_items + cheese_fries_cost

    # L4
    money_spent_percent = 0.8 # spend 80% of their combined money
    total_money_start = total_meal_cost / money_spent_percent

    # L5
    jim_money = 20 # Jim brought $20
    cousin_money = total_money_start - jim_money

    # FA
    answer = cousin_money
    return answer