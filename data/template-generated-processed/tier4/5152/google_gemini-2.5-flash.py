def solve():
    """Index: 5152.
    Returns: the cost of Jimmy's pizza per slice.
    """
    # L1
    base_pizza_cost = 10.00 # The large pizza costs $10.00
    first_topping_cost = 2.00 # The first topping costs $2.00
    cost_after_first_topping = base_pizza_cost + first_topping_cost

    # L2
    num_next_toppings = 2 # the next 2 toppings
    cost_per_next_topping = 1.00 # cost $1.00 each
    cost_next_two_toppings = num_next_toppings * cost_per_next_topping

    # L3
    num_remaining_toppings = 4 # olives, mushrooms, bell peppers and pineapple (4 toppings)
    cost_per_remaining_topping = 0.50 # the rest of the toppings cost $0.50
    cost_remaining_toppings = num_remaining_toppings * cost_per_remaining_topping

    # L4
    total_pizza_cost = cost_after_first_topping + cost_next_two_toppings + cost_remaining_toppings

    # L5
    num_slices = 8 # is cut into 8 slices
    cost_per_slice = total_pizza_cost / num_slices

    # FA
    answer = cost_per_slice
    return answer