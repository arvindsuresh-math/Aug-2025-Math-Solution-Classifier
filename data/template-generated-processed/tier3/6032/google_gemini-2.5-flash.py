def solve():
    """Index: 6032.
    Returns: the cost of one chair.
    """
    # L1
    total_spent = 56 # spent $56
    table_cost = 34 # bought a table for $34
    cost_on_chairs = total_spent - table_cost

    # L2
    number_of_chairs = 2 # 2 chairs
    cost_per_chair = cost_on_chairs / number_of_chairs

    # FA
    answer = cost_per_chair
    return answer