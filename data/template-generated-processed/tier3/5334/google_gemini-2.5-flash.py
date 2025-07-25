def solve():
    """Index: 5334.
    Returns: the total amount Judy will spend on pencils.
    """
    # L1
    pencils_per_school_week = 10 # 10 pencils
    school_days_per_week = 5 # 5 day school week
    pencils_per_day = pencils_per_school_week / school_days_per_week

    # L2
    total_days = 45 # over 45 days
    total_pencils_needed = pencils_per_day * total_days

    # L3
    pencils_per_pack = 30 # A 30 pack of pencils
    packs_needed = total_pencils_needed / pencils_per_pack

    # L4
    cost_per_pack = 4 # costs $4
    total_cost = packs_needed * cost_per_pack

    # FA
    answer = total_cost
    return answer