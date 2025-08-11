def solve():
    """Index: 4839.
    Returns: the amount each person paid for the cupcakes.
    """
    # L1
    cupcake_cost = 1.50 # Each cupcake cost $1.50
    num_cupcakes = 12 # bought 12 cupcakes together
    total_cost = cupcake_cost * num_cupcakes

    # L2
    num_people = 2 # John and his best friend Steve
    cost_per_person = total_cost / num_people

    # FA
    answer = cost_per_person
    return answer