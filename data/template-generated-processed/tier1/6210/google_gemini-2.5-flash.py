def solve():
    """Index: 6210.
    Returns: the total number of pieces of pizza the children are carrying.
    """
    # L1
    pizzas_per_grader = 20 # 20 pizzas
    pieces_per_pizza = 6 # 6 pieces of pizza
    pieces_per_grader = pizzas_per_grader * pieces_per_pizza

    # L2
    num_fourth_graders = 10 # Ten fourth-graders
    total_pieces = pieces_per_grader * num_fourth_graders

    # FA
    answer = total_pieces
    return answer