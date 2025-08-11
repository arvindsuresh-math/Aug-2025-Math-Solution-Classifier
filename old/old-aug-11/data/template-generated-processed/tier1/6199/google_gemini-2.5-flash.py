def solve():
    """Index: 6199.
    Returns: the number of floors Building C has.
    """
    # L1
    building_a_floors = 4 # Building A has 4 floors

    # L2
    less_than_b = 9 # 9 less than Building B
    building_b_floors = building_a_floors + less_than_b

    # L3
    multiplier_for_b = 5 # five times as many floors
    less_than_five_times_b = 6 # six less than five times as many floors
    building_c_floors = (building_b_floors * multiplier_for_b) - less_than_five_times_b

    # FA
    answer = building_c_floors
    return answer