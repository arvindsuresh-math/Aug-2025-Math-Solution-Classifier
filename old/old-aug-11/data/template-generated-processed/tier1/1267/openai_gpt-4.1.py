def solve():
    """Index: 1267.
    Returns: the amount of money left in Liza's account after all transactions.
    """
    # L1
    initial_balance = 800 # $800 in her checking account
    rent = 450 # paid her rent, $450
    after_rent = initial_balance - rent

    # L2
    paycheck = 1500 # deposited her $1500 paycheck
    after_paycheck = after_rent + paycheck

    # L3
    electricity_bill = 117 # electricity bill, $117
    internet_bill = 100 # internet bill, $100
    total_utilities = electricity_bill + internet_bill

    # L4
    after_utilities = after_paycheck - total_utilities

    # L5
    phone_bill = 70 # phone bill, $70
    after_phone = after_utilities - phone_bill

    # FA
    answer = after_phone
    return answer