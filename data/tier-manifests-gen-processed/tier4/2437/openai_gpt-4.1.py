def solve():
    """Index: 2437.
    Returns: the number of dollars remaining in Emma's account after withdrawing $5 bills.
    """
    # L1
    days_in_week = 7 # Each day of the week
    daily_spending = 8 # she spends $8
    total_spent = days_in_week * daily_spending

    # L2
    initial_balance = 100 # Emma's bank account has $100
    balance_after_spending = initial_balance - total_spent

    # L3
    bill_denomination = 5 # $5 bills
    num_bills_float = balance_after_spending / bill_denomination
    num_bills = int(num_bills_float)

    # L4
    total_withdrawn = num_bills * bill_denomination

    # L5
    remaining_balance = balance_after_spending - total_withdrawn

    # FA
    answer = remaining_balance
    return answer