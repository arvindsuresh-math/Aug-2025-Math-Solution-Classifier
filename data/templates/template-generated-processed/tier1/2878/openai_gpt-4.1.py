def solve():
    """Index: 2878.
    Returns: the total number of watts used if all lights are left on for two hours.
    """
    # L1
    bedroom_wph = 6 # 6 watts per hour
    hours_on = 2 # two hours
    bedroom_total = bedroom_wph * hours_on

    # L2
    office_multiplier = 3 # 3 times as many watts as his bedroom light
    office_wph = office_multiplier * bedroom_wph

    # L3
    office_total = office_wph * hours_on

    # L4
    living_multiplier = 4 # 4 times as many watts as his bedroom light
    living_wph = living_multiplier * bedroom_wph

    # L5
    living_total = living_wph * hours_on

    # L6
    total_watts = bedroom_total + office_total + living_total

    # FA
    answer = total_watts
    return answer