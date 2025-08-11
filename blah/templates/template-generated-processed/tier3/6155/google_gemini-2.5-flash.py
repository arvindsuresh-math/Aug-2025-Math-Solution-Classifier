def solve():
    """Index: 6155.
    Returns: the time in hours to fill 25 cans to full capacity.
    """
    # L1
    can_capacity = 8 # eight gallon water cans
    quarter_denominator = 4 # three quarters of its capacity
    quarter_numerator = 3 # three quarters of its capacity
    gallons_per_partial_can = can_capacity / quarter_denominator * quarter_numerator

    # L2
    num_cans_initial = 20 # 20 eight gallon water cans
    total_gallons_initial_fill = gallons_per_partial_can * num_cans_initial

    # L3
    time_initial_hours = 3 # in three hours
    gallons_per_hour = total_gallons_initial_fill / time_initial_hours

    # L4
    num_cans_new = 25 # fill 25 cans
    total_gallons_new_fill = num_cans_new * can_capacity

    # L5
    time_to_fill_new_cans = total_gallons_new_fill / gallons_per_hour

    # FA
    answer = time_to_fill_new_cans
    return answer