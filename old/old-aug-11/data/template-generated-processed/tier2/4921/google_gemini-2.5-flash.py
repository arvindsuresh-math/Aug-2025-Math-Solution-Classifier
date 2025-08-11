def solve():
    """Index: 4921.
    Returns: the total amount of money Tyrone has.
    """
    # L1
    num_one_dollar_bills = 2 # two $1 bills
    value_one_dollar_bill = 1 # WK
    total_one_dollar_bills = num_one_dollar_bills * value_one_dollar_bill

    # L2
    num_five_dollar_bills = 1 # a $5 bill
    value_five_dollar_bill = 5 # WK
    total_five_dollar_bills = num_five_dollar_bills * value_five_dollar_bill

    # L3
    num_quarters = 13 # 13 quarters
    value_quarter = 0.25 # WK
    total_quarters = num_quarters * value_quarter

    # L4
    num_dimes = 20 # 20 dimes
    value_dime = 0.1 # WK
    total_dimes = num_dimes * value_dime

    # L5
    num_nickels = 8 # 8 nickels
    value_nickel = 0.05 # WK
    total_nickels = num_nickels * value_nickel

    # L6
    num_pennies = 35 # 35 pennies
    value_penny = 0.01 # WK
    total_pennies = num_pennies * value_penny

    # L7
    total_money = total_one_dollar_bills + total_five_dollar_bills + total_quarters + total_dimes + total_nickels + total_pennies

    # FA
    answer = total_money
    return answer