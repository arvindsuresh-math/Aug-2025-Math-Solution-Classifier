def solve():
    """Index: 6652.
    Returns: the total money the store made from sales.
    """
    # L1
    num_eraser_pencils = 200 # sell 200 pencils with an eraser
    cost_eraser_pencil = 0.8 # costs $0.8 each
    total_eraser_pencil_sales = num_eraser_pencils * cost_eraser_pencil

    # L2
    num_regular_pencils = 40 # 40 regular pencils
    cost_regular_pencil = 0.5 # regular pencil for $0.5 each
    total_regular_pencil_sales = num_regular_pencils * cost_regular_pencil

    # L3
    num_short_pencils = 35 # 35 short pencils
    cost_short_pencil = 0.4 # short pencil for $0.4 each
    total_short_pencil_sales = num_short_pencils * cost_short_pencil

    # L4
    total_sales = total_eraser_pencil_sales + total_regular_pencil_sales + total_short_pencil_sales

    # FA
    answer = total_sales
    return answer