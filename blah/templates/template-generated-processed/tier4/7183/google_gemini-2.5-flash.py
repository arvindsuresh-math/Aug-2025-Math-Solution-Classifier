def solve():
    """Index: 7183.
    Returns: the distance the train can travel.
    """
    # L1
    miles_per_coal_unit_numerator = 5 # 5 miles
    miles_per_coal_unit_denominator = 2 # 2 pounds of coal
    miles_per_pound = miles_per_coal_unit_numerator / miles_per_coal_unit_denominator

    # L2
    remaining_coal = 160 # 160 pounds of coal remaining
    total_distance = remaining_coal * miles_per_pound

    # FA
    answer = total_distance
    return answer