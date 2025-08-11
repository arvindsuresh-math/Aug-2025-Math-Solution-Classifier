def solve():
    """Index: 3690.
    Returns: Sandy's monthly phone bill expense.
    """
    # L1
    kim_current_age = 10 # Kim is currently 10 years old
    years_later = 2 # In two years
    kim_age_in_two_years = kim_current_age + years_later

    # L2
    sandy_age_multiplier = 3 # three times as old as Kim
    sandy_age_in_two_years = sandy_age_multiplier * kim_age_in_two_years

    # L3
    sandy_current_age = sandy_age_in_two_years - years_later

    # L4
    bill_multiplier = 10 # ten times her age now
    sandy_phone_bill = bill_multiplier * sandy_current_age

    # FA
    answer = sandy_phone_bill
    return answer