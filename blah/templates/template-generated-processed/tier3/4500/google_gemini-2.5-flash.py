from fractions import Fraction

def solve():
    """Index: 4500.
    Returns: the total number of pieces of bills Uncle Bradley will have.
    """
    # L1
    total_money = 1000 # a $1000 bill
    fraction_for_50_bills = Fraction(3, 10) # 3/10 of the money
    money_for_50_bills = total_money * fraction_for_50_bills

    # L2
    fifty_dollar_bill_value = 50 # $50 bills
    num_50_dollar_bills = money_for_50_bills / fifty_dollar_bill_value

    # L3
    money_for_100_bills = total_money - money_for_50_bills

    # L4
    hundred_dollar_bill_value = 100 # $100 bills
    num_100_dollar_bills = money_for_100_bills / hundred_dollar_bill_value

    # L5
    total_pieces_of_bills = num_50_dollar_bills + num_100_dollar_bills

    # FA
    answer = total_pieces_of_bills
    return answer