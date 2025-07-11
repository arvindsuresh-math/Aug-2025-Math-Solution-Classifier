def solve():
    """Index: 2878.
    Returns: the total watts used by all lights in two hours.
    """
    # L1
    bedroom_watt_per_hour = 6 # 6 watts per hour
    hours_on = 2 # two hours
    bedroom_total_watts = bedroom_watt_per_hour * hours_on

    # L2
    office_multiplier = 3 # three times as much energy
    office_watt_per_hour = office_multiplier * bedroom_watt_per_hour

    # L3
    office_total_watts = office_watt_per_hour * hours_on

    # L4
    living_room_multiplier = 4 # four times as much energy
    living_room_watt_per_hour = living_room_multiplier * bedroom_watt_per_hour

    # L5
    living_room_total_watts = living_room_watt_per_hour * hours_on

    # L6
    total_watts_used = bedroom_total_watts + office_total_watts + living_room_total_watts

    # FA
    answer = total_watts_used
    return answer