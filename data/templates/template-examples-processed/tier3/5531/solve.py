def solve():
    """Index: 5531.
    Returns: the total amount of Dakota's medical bill.
    """
    # L1
    days_in_hospital = 3 # 3 days in the hospital
    bed_cost_per_day = 900 # $900/day for her bed
    total_bed_cost = bed_cost_per_day * days_in_hospital

    # L2
    time_per_specialist = 15 # 15 minutes each
    num_specialists = 2 # two specialists
    total_specialist_minutes = time_per_specialist * num_specialists

    # L3
    minutes_per_hour = 60 # WK
    specialist_hourly_rate = 250 # $250/hour for two specialists
    total_specialist_charge = total_specialist_minutes / minutes_per_hour * specialist_hourly_rate

    # L4
    ambulance_cost = 1800 # $1800 for the ambulance ride
    total_bill = total_bed_cost + ambulance_cost + total_specialist_charge

    # FA
    answer = total_bill
    return answer