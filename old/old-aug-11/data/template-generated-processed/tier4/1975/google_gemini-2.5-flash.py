def solve():
    """Index: 1975.
    Returns: the amount of money now in the account.
    """
    # L1
    initial_deposit = 1000 # $1,000 in a savings account
    first_year_interest_rate = 0.2 # earns 20% interest
    first_year_interest_earned = initial_deposit * first_year_interest_rate

    # L2
    balance_after_year1 = initial_deposit + first_year_interest_earned

    # L3
    withdrawal_divisor = 2 # takes out half the money
    amount_withdrawn = balance_after_year1 / withdrawal_divisor

    # L4
    remaining_balance_after_withdrawal = balance_after_year1 - amount_withdrawn

    # L5
    second_year_interest_rate = 0.15 # remaining money earns 15% interest
    second_year_interest_earned = remaining_balance_after_withdrawal * second_year_interest_rate

    # L6
    final_balance = remaining_balance_after_withdrawal + second_year_interest_earned

    # FA
    answer = final_balance
    return answer