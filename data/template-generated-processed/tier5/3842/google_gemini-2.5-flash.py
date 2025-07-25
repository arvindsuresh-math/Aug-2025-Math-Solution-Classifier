def solve():
    """Index: 3842.
    Returns: the price of the pants.
    """
    # Define initial variables from the problem statement that are used in computations.
    # These are not tied to a specific L-line as they are setup/equation definition.
    shirt_fraction_value = 3/4 # price of a shirt is three-quarters of the price of the pants
    shoes_extra_cost_value = 10 # price of a shoe is ten dollars more than the price of the pants
    total_cost_value = 340 # bought a shirt, pants, and shoes for $340

    # L3
    combined_coefficient = 1 + shirt_fraction_value + 1

    # L4
    total_after_subtraction = total_cost_value - shoes_extra_cost_value

    # L5
    price_of_pants = total_after_subtraction / combined_coefficient

    # FA
    answer = price_of_pants
    return answer