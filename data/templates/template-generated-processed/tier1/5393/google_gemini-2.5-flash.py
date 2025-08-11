def solve():
    """Index: 5393.
    Returns: the total cost of the modular home in dollars.
    """
    # L1
    kitchen_sq_ft = 400 # A 400 square foot Kitchen module
    bathroom_sq_ft = 150 # a 150 square foot bathroom module
    total_home_sq_ft = 2000 # a 2,000 square foot modular home
    modules_sq_ft = kitchen_sq_ft + bathroom_sq_ft + bathroom_sq_ft

    # L2
    remaining_sq_ft = total_home_sq_ft - modules_sq_ft

    # L3
    kitchen_cost = 20000 # A 400 square foot Kitchen module costs $20000
    bathroom_cost = 12000 # a 150 square foot bathroom module costs $12,000
    modules_cost = kitchen_cost + bathroom_cost + bathroom_cost

    # L4
    other_module_cost_per_sq_ft = 100 # All other modules cost $100 per square foot
    other_modules_cost = remaining_sq_ft * other_module_cost_per_sq_ft

    # L5
    total_cost = modules_cost + other_modules_cost

    # FA
    answer = total_cost
    return answer