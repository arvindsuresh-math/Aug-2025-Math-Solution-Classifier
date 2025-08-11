def solve():
    """Index: 6874.
    Returns: the total amount Mandy paid for data in the first 6 months.
    """
    # L1
    data_plan_charge = 30 # $30 per month for data
    promotional_fraction_numerator = 1 # one-third the normal price
    promotional_fraction_denominator = 3 # one-third the normal price
    first_month_charge = data_plan_charge / promotional_fraction_denominator

    # L2
    extra_fee = 15 # an extra fee of $15
    fourth_month_charge = data_plan_charge + extra_fee

    # L3
    total_months = 6 # first 6 months
    special_months = 2 # WK
    regular_charge_months = total_months - special_months

    # L4
    regular_charge_total = regular_charge_months * data_plan_charge
    special_months_total = first_month_charge + fourth_month_charge
    total_paid = regular_charge_total + special_months_total

    # FA
    answer = total_paid
    return answer