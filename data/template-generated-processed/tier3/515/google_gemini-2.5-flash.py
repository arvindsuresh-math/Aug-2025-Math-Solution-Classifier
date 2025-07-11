def solve():
    """Index: 515.
    Returns: the percentage chance of Annie getting into a serious accident.
    """
    # L1
    initial_temperature = 32 # 32 degrees
    current_temperature = 8 # temperature is 8 degrees
    temperature_drop = initial_temperature - current_temperature

    # L2
    degrees_per_skid_risk_increase = 3 # For every 3 degrees the temperature drops
    num_skid_increases = temperature_drop / degrees_per_skid_risk_increase

    # L3
    skid_risk_percentage_per_increase = 5 # increase 5%
    total_skid_risk_percentage = num_skid_increases * skid_risk_percentage_per_increase

    # L4
    total_percentage_base = 100 # 100%
    regain_control_percentage = 40 # 40% of regaining control
    accident_if_skid_percentage = total_percentage_base - regain_control_percentage

    # L5
    total_accident_risk_percentage = (accident_if_skid_percentage * total_skid_risk_percentage) / 100

    # FA
    answer = total_accident_risk_percentage
    return answer