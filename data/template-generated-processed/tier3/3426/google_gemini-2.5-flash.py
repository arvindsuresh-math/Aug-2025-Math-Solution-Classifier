def solve():
    """Index: 3426.
    Returns: the total number of pieces of bills Lorie will have.
    """
    # L1
    bill_value_100 = 100 # $100 bills
    bill_value_50 = 50 # $50 bills
    pieces_of_50_from_first_100 = bill_value_100 / bill_value_50

    # L2
    half_divisor = 2 # Half of the remaining $100 bill
    value_of_half_100_bill = bill_value_100 / half_divisor

    # L3
    bill_value_10 = 10 # $10 bills
    pieces_of_10_from_half_100 = value_of_half_100_bill / bill_value_10

    # L4
    bill_value_5 = 5 # $5 bills
    pieces_of_5_from_other_half_100 = value_of_half_100_bill / bill_value_5

    # L5
    total_pieces_of_bills = pieces_of_50_from_first_100 + pieces_of_10_from_half_100 + pieces_of_5_from_other_half_100

    # FA
    answer = total_pieces_of_bills
    return answer