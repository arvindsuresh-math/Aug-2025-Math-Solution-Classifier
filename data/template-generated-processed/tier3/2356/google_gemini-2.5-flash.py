def solve():
    """Index: 2356.
    Returns: the cost of 1 kg of apples.
    """
    # L1
    total_cost_oranges = 12 # The total cost of oranges was $12
    cheaper_factor = 2 # The apples were two times cheaper than the oranges
    cost_of_apples_total = total_cost_oranges / cheaper_factor

    # L2
    quantity_apples_kg = 3 # 3 kg of apples
    cost_per_kg_apples = cost_of_apples_total / quantity_apples_kg

    # FA
    answer = cost_per_kg_apples
    return answer