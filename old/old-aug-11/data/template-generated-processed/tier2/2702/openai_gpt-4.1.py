def solve():
    """Index: 2702.
    Returns: the number of pizza slices left over after Stephen and Pete eat.
    """
    # L1
    num_pizzas = 2 # 2 large pizzas
    slices_per_pizza = 12 # each cut into 12 slices
    total_slices = num_pizzas * slices_per_pizza

    # L2
    stephen_percent_num = 25 # 25% of the pizza
    stephen_percent_decimal = 0.25 # .25*24
    percent_factor = 0.01 # WK
    stephen_slices = stephen_percent_num * percent_factor * total_slices

    # L3
    after_stephen_slices = total_slices - stephen_slices

    # L4
    pete_percent_decimal = 0.50 # .50
    pete_percent_num = 50 # 50% of 18 slices
    pete_slices = after_stephen_slices * pete_percent_num * percent_factor

    # L5
    answer = after_stephen_slices - pete_slices
    return answer