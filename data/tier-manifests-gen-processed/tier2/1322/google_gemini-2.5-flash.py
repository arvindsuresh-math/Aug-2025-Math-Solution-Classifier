def solve():
    """Index: 1322.
    Returns: the amount Tom spends.
    """
    # L1
    num_seats = 500 # 500 seat theater
    sq_ft_per_seat = 12 # 12 square feet for every seat
    total_sq_feet = num_seats * sq_ft_per_seat

    # L2
    cost_per_sq_ft = 5 # $5 per square foot
    land_cost = cost_per_sq_ft * total_sq_feet

    # L3
    construction_cost_factor = 2 # construction will cost twice as much as the land
    construction_cost = land_cost * construction_cost_factor

    # L4
    total_project_cost = construction_cost + land_cost

    # L5
    partner_coverage_percent = 0.4 # covers 40% of the cost
    partner_covered_amount = total_project_cost * partner_coverage_percent

    # L6
    tom_cost = total_project_cost - partner_covered_amount

    # FA
    answer = tom_cost
    return answer