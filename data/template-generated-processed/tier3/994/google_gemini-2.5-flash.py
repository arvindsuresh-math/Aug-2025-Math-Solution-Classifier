def solve():
    """Index: 994.
    Returns: the total number of slices left over.
    """
    # L1
    num_pizzas = 2 # Dean ordered 2 large pizzas
    slices_per_pizza = 12 # each cut into 12 slices
    total_initial_slices = num_pizzas * slices_per_pizza

    # L2
    dean_ate_divisor = 2 # ate half of the Hawaiian pizza
    dean_eaten_slices = slices_per_pizza / dean_ate_divisor

    # L3
    sammy_ate_divisor = 3 # Sammy ate a third of the cheese pizza
    sammy_eaten_slices = slices_per_pizza / sammy_ate_divisor

    # L4
    frank_ate_slices = 3 # Frank only ate 3 slices of Hawaiian pizza
    total_eaten_slices = dean_eaten_slices + sammy_eaten_slices + frank_ate_slices

    # L5
    slices_left_over = total_initial_slices - total_eaten_slices

    # FA
    answer = slices_left_over
    return answer