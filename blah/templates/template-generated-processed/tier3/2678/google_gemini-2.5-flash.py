def solve():
    """Index: 2678.
    Returns: the total number of pizzas Nunzio eats.
    """
    # L1
    pieces_per_day = 3 # three pieces of pizza every day
    number_of_days = 72 # 72 days
    total_pieces_eaten = number_of_days * pieces_per_day

    # L2
    pieces_per_pizza = 8 # one-eighth of the entire pie
    total_pizzas_eaten = total_pieces_eaten / pieces_per_pizza

    # FA
    answer = total_pizzas_eaten
    return answer