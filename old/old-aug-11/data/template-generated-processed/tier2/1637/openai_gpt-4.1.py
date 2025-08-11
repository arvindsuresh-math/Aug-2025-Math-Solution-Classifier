def solve():
    """Index: 1637.
    Returns: the total amount Lennon will be reimbursed for mileage.
    """
    # L1
    monday_miles = 18 # Monday he drove 18 miles
    tuesday_miles = 26 # Tuesday he drove 26 miles
    wednesday_miles = 20 # Wednesday he drove 20 miles
    thursday_miles = 20 # Thursday he drove 20 miles
    friday_miles = 16 # Friday he drove 16 miles
    total_miles = monday_miles + tuesday_miles + wednesday_miles + thursday_miles + friday_miles

    # L2
    reimbursement_per_mile = 0.36 # paid $0.36 in mileage reimbursement
    total_reimbursement = reimbursement_per_mile * total_miles

    # FA
    answer = total_reimbursement
    return answer