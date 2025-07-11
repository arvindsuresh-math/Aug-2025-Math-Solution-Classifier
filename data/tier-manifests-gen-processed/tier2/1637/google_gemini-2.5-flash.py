def solve():
    """Index: 1637.
    Returns: the total money Lennon will be reimbursed.
    """
    # L1
    monday_miles = 18 # On Monday he drove 18 miles
    tuesday_miles = 26 # Tuesday he drove 26 miles
    wednesday_miles = 20 # Wednesday and Thursday he drove 20 miles each day
    thursday_miles = 20 # Wednesday and Thursday he drove 20 miles each day
    friday_miles = 16 # on Friday he drove 16 miles
    total_miles = monday_miles + tuesday_miles + wednesday_miles + thursday_miles + friday_miles

    # L2
    mileage_rate = 0.36 # paid $0.36 in mileage reimbursement
    reimbursement_amount = mileage_rate * total_miles

    # FA
    answer = reimbursement_amount
    return answer