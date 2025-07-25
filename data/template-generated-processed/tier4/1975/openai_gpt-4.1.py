def solve():
    """Index: 1975.
    Returns: the amount now in the account after two years and withdrawals.
    """
    # L1
    initial_deposit = 1000 # Tony puts $1,000 in a savings account
    first_year_interest_rate = 0.2 # earns 20% interest
    first_year_interest = initial_deposit * first_year_interest_rate

    # L2
    after_first_year = initial_deposit + first_year_interest

    # L3
    withdrawal_fraction = 2 # takes out half the money
    withdrawal_amount = after_first_year / withdrawal_fraction

    # L4
    after_withdrawal = after_first_year - withdrawal_amount

    # L5
    second_year_interest_rate = 0.15 # remaining money earns 15% interest
    second_year_interest = after_withdrawal * second_year_interest_rate

    # L6
    final_amount = after_withdrawal + second_year_interest

    # FA
    answer = final_amount
    return answer