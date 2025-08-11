def solve():
    """Index: 3826.
    Returns: the amount Greg spent on a shirt.
    """
    # L5
    total_spent = 300 # spent 300$ on a shirt and shoes
    extra_on_shoes = 9 # 9 more than twice as much on shoes
    value_after_subtraction = total_spent - extra_on_shoes

    coefficient_of_x_shirt = 1 # WK
    coefficient_of_x_shoes = 2 # twice as much on shoes as he did a shirt
    three_x_coefficient = coefficient_of_x_shirt + coefficient_of_x_shoes

    # L6
    shirt_cost = value_after_subtraction / three_x_coefficient

    # FA
    answer = shirt_cost
    return answer