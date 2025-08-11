def solve():
    """Index: 7213.
    Returns: the combined total cost of Mike and John's lunch.
    """
    # L3
    mike_salad_cost = 2 # a side salad for $2
    mike_fries_cost = 4 # a plate of cheesy fries for $4
    mike_cola_cost = 2 # a diet cola for $2
    mike_extra_cost = mike_salad_cost + mike_fries_cost + mike_cola_cost

    # L4
    # The solution implies solving 2x = x + mike_extra_cost, which simplifies to x = mike_extra_cost
    taco_grande_cost = mike_extra_cost

    # L5
    # Combined total cost = John's bill + Mike's bill
    # John's bill = taco_grande_cost
    # Mike's bill = taco_grande_cost + mike_salad_cost + mike_fries_cost + mike_cola_cost
    combined_total_cost = taco_grande_cost + taco_grande_cost + mike_salad_cost + mike_fries_cost + mike_cola_cost

    # FA
    answer = combined_total_cost
    return answer