def solve():
    """Index: 5776.
    Returns: the total cost of the sunscreen.
    """
    # L1
    total_hours = 16 # 16 hours
    reapply_interval_hours = 2 # re-apply sunscreen after 2 hours
    num_applications = total_hours / reapply_interval_hours

    # L2
    ounces_per_application = 3 # 3 ounces of sunscreen each application
    total_ounces_needed = ounces_per_application * num_applications

    # L3
    ounces_per_bottle = 12 # a bottle contain 12 ounces
    num_bottles_needed = total_ounces_needed / ounces_per_bottle

    # L4
    cost_per_bottle = 3.5 # costs $3.5
    total_cost = num_bottles_needed * cost_per_bottle

    # FA
    answer = total_cost
    return answer