def solve():
    """Index: 7356.
    Returns: the total number of topping combinations Denmark has.
    """
    # L1
    num_cheese_options = 3 # 3 cheese
    num_meat_options = 4 # 4 meat
    num_vegetable_options = 5 # 5 vegetable options
    total_combinations_initial = num_cheese_options * num_meat_options * num_vegetable_options

    # L2
    # The solution's calculation for "bad choices" is unusual (1+1+1=3).
    # It seems to count the number of categories involved in the restriction rather than combinations.
    # Following the solution's explicit calculation.
    restricted_cheese_count = 1 # one selection from each topping category
    restricted_meat_count = 1 # if he chooses to have pepperoni
    restricted_vegetable_count = 1 # he cannot have peppers
    bad_choices = restricted_cheese_count + restricted_meat_count + restricted_vegetable_count

    # L3
    final_choices = total_combinations_initial - bad_choices

    # FA
    answer = final_choices
    return answer