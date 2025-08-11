def solve():
    """Index: 5269.
    Returns: the total amount of the school fee.
    """
    # L1
    mother_50_bills = 1 # one $50 bill
    father_50_bills = 4 # four $50 bills
    total_50_bills = mother_50_bills + father_50_bills

    # L2
    denomination_50 = 50 # $50 bill
    amount_50_bills = denomination_50 * total_50_bills

    # L3
    mother_20_bills = 2 # two $20 bills
    father_20_bills = 1 # one $20 bill
    total_20_bills = mother_20_bills + father_20_bills

    # L4
    denomination_20 = 20 # $20 bill
    amount_20_bills = denomination_20 * total_20_bills

    # L5
    mother_10_bills = 3 # three $10 bills
    father_10_bills = 1 # one $10 bill
    total_10_bills = mother_10_bills + father_10_bills

    # L6
    denomination_10 = 10 # $10 bill
    amount_10_bills = denomination_10 * total_10_bills

    # L7
    school_fee = amount_50_bills + amount_20_bills + amount_10_bills

    # FA
    answer = school_fee
    return answer