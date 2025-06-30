def solve_53():
    # Given quantities and prices
    num_ice_cream_cartons = 10
    cost_per_ice_cream_carton = 4
    num_frozen_yogurt_cartons = 4
    cost_per_frozen_yogurt_carton = 1

    # Calculate the total cost of ice cream
    total_cost_ice_cream = num_ice_cream_cartons * cost_per_ice_cream_carton

    # Calculate the total cost of frozen yogurt
    total_cost_frozen_yogurt = num_frozen_yogurt_cartons * cost_per_frozen_yogurt_carton

    # Calculate how much more was spent on ice cream than on frozen yogurt
    difference_in_cost = total_cost_ice_cream - total_cost_frozen_yogurt

    return difference_in_cost

# The final answer is the result of the function call.
# print(solve_53())