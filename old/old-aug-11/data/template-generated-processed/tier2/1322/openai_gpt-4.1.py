def solve():
    """Index: 1322.
    Returns: the amount Tom spends on the theater after his partner's contribution.
    """
    # L1
    num_seats = 500 # 500 seat theater
    sqft_per_seat = 12 # 12 square feet for every seat
    total_sqft = num_seats * sqft_per_seat

    # L2
    land_cost_per_sqft = 5 # $5 per square foot
    land_cost = land_cost_per_sqft * total_sqft

    # L3
    construction_multiplier = 2 # construction will cost twice as much as the land
    construction_cost = land_cost * construction_multiplier

    # L4
    total_cost = construction_cost + land_cost

    # L5
    partner_share_percent = 0.4 # partner covers 40% of the cost
    partner_share = total_cost * partner_share_percent

    # L6
    tom_cost = total_cost - partner_share

    # FA
    answer = tom_cost
    return answer