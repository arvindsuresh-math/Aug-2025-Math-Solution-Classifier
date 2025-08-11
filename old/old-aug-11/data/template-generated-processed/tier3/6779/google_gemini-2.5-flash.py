def solve():
    """Index: 6779.
    Returns: the difference in the number of $10 bills Manny and Mandy will have.
    """
    # L1
    mandy_bill_denomination = 20 # three $20 bills
    mandy_num_bills = 3 # three $20 bills
    mandy_total_money = mandy_bill_denomination * mandy_num_bills

    # L2
    exchange_denomination = 10 # for $10 bills
    mandy_num_ten_dollar_bills = mandy_total_money / exchange_denomination

    # L3
    manny_bill_denomination = 50 # two $50 bills
    manny_num_bills = 2 # two $50 bills
    manny_total_money = manny_bill_denomination * manny_num_bills

    # L4
    manny_num_ten_dollar_bills = manny_total_money / exchange_denomination

    # L5
    difference_in_ten_dollar_bills = manny_num_ten_dollar_bills - mandy_num_ten_dollar_bills

    # FA
    answer = difference_in_ten_dollar_bills
    return answer