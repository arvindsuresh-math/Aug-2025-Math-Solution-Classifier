def solve():
    """Index: 1267.
    Returns: the amount of money left in Liza's account.
    """
    # L1
    initial_balance = 800 # On Tuesday, Liza had $800 in her checking account
    rent_paid = 450 # she paid her rent, $450
    balance_after_rent = initial_balance - rent_paid

    # L2
    paycheck_deposited = 1500 # she deposited her $1500 paycheck
    balance_after_deposit = balance_after_rent + paycheck_deposited

    # L3
    electricity_bill = 117 # electricity and internet bills which were $117
    internet_bill = 100 # and $100, respectively
    total_friday_bills = electricity_bill + internet_bill

    # L4
    balance_after_friday_bills = balance_after_deposit - total_friday_bills

    # L5
    phone_bill = 70 # she paid her phone bill, $70
    final_balance = balance_after_friday_bills - phone_bill

    # FA
    answer = final_balance
    return answer