def solve():
    """Index: 4253.
    Returns: the number of grilled cheese sandwiches Joan makes.
    """
    # L1
    num_ham_sandwiches = 10 # If she makes 10 ham sandwiches
    slices_per_ham_sandwich = 2 # One ham sandwich requires 2 slices of cheese
    cheese_for_ham_sandwiches = num_ham_sandwiches * slices_per_ham_sandwich

    # L2
    total_cheese_slices = 50 # She uses a total of 50 slices of cheese
    cheese_for_grilled_cheese = total_cheese_slices - cheese_for_ham_sandwiches

    # L3
    slices_per_grilled_cheese = 3 # one grilled cheese sandwich requires 3 slices of cheese
    num_grilled_cheese_sandwiches = cheese_for_grilled_cheese / slices_per_grilled_cheese

    # FA
    answer = num_grilled_cheese_sandwiches
    return answer