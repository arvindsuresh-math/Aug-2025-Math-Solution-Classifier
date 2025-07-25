def solve():
    """Index: 5531.
    Returns: the total amount of Dakota's medical bill.
    """
    # L1
    cost_per_day_bed = 900 # $900/day for her bed
    days_in_hospital = 3 # 3 days in the hospital
    cost_hospital_bed = cost_per_day_bed * days_in_hospital

    # L2
    minutes_per_specialist = 15 # 15 minutes each
    num_specialists = 2 # two specialists
    total_specialist_minutes = minutes_per_specialist * num_specialists

    # L3
    minutes_per_hour = 60 # WK
    specialist_hourly_rate = 250 # $250/hour
    cost_specialists = total_specialist_minutes / minutes_per_hour * specialist_hourly_rate

    # L4
    cost_ambulance_ride = 1800 # $1800 for the ambulance ride
    total_bill = cost_hospital_bed + cost_ambulance_ride + cost_specialists

    # FA
    answer = total_bill
    return answer