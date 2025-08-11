def solve():
    """Index: 3035.
    Returns: the number of hours Linda needs to babysit to cover the application fees.
    """
    # L1
    fee_per_college = 25.00 # $25.00 application fee
    num_colleges = 6 # applying to 6 colleges
    total_application_fees = fee_per_college * num_colleges

    # L2
    hourly_rate = 10.00 # $10.00 an hour babysitting
    hours_needed = total_application_fees / hourly_rate

    # FA
    answer = hours_needed
    return answer