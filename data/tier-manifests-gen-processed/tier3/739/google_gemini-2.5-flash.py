def solve():
    """Index: 739.
    Returns: the number of people the vampire needs to suck each day.
    """
    # L1
    weekly_blood_needed_gallons = 7 # 7 gallons of blood per week
    days_per_week = 7 # WK
    daily_blood_needed_gallons = weekly_blood_needed_gallons / days_per_week

    # L2
    total_ounces_per_gallon = 128 # WK
    ounces_per_pint = 16 # WK
    pints_per_gallon = total_ounces_per_gallon / ounces_per_pint

    # L3
    daily_pints_required = daily_blood_needed_gallons * pints_per_gallon
    pints_per_person = 2 # 2 pints of blood per person
    people_per_day = daily_pints_required / pints_per_person

    # FA
    answer = people_per_day
    return answer