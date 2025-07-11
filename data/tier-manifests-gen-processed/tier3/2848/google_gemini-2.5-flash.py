def solve():
    """Index: 2848.
    Returns: the amount each person will contribute to the cost of the paint.
    """
    # L1
    total_area = 1600 # their walls have a total area of 1600 square feet
    coverage_per_gallon = 400 # can cover up to 400 square feet
    gallons_for_first_coat = total_area / coverage_per_gallon

    # L2
    num_coats = 2 # will need a second coat
    total_gallons_needed = gallons_for_first_coat * num_coats

    # L3
    cost_per_gallon = 45 # A gallon of paint costs $45
    total_cost_of_paint = cost_per_gallon * total_gallons_needed

    # L4
    num_people_splitting_cost = 2 # Jason and Jeremy... agreed to split the cost
    contribution_per_person = total_cost_of_paint / num_people_splitting_cost

    # FA
    answer = contribution_per_person
    return answer