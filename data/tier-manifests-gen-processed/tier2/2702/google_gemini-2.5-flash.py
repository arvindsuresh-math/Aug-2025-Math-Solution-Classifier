def solve():
    """Index: 2702.
    Returns: the number of slices left over.
    """
    # L1
    num_pizzas = 2 # 2 large pizzas
    slices_per_pizza = 12 # cut into 12 slices
    total_slices = num_pizzas * slices_per_pizza

    # L2
    stephen_ate_percent_num = 25 # 25% of the pizza
    stephen_ate_percent_decimal = 0.25 # 25% of the pizza
    percent_factor = 0.01 # WK
    stephen_slices_eaten = stephen_ate_percent_num * percent_factor * total_slices

    # L3
    slices_after_stephen = total_slices - stephen_slices_eaten

    # L4
    pete_ate_percent_num = 50 # 50% of the remaining pizza
    pete_ate_percent_decimal = 0.50 # 50% of the remaining pizza
    pete_slices_eaten = slices_after_stephen * pete_ate_percent_decimal

    # L5
    slices_left_over = slices_after_stephen - pete_slices_eaten

    # FA
    answer = slices_left_over
    return answer