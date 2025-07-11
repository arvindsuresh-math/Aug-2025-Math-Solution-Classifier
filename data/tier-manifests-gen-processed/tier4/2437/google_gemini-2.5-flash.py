def solve():
    """Index: 2437.
    Returns: the number of dollars remaining in the account.
    """
    # L1
    days_in_week = 7 # WK
    daily_spending = 8 # she spends $8
    weekly_spending = days_in_week * daily_spending

    # L2
    initial_balance = 100 # Emma's bank account has $100 in it
    balance_after_spending = initial_balance - weekly_spending

    # L3
    bill_denomination = 5 # $5 bills
    num_bills_float = balance_after_spending / bill_denomination
    num_bills_to_take = int(num_bills_float) # as many $5 bills as her account can give her

    # L4
    amount_withdrawn = num_bills_to_take * bill_denomination

    # L5
    remaining_balance = balance_after_spending - amount_withdrawn

    # FA
    answer = remaining_balance
    return answer