def solve():
    """Index: 7237.
    Returns: the total amount Jack will have in his piggy bank.
    """
    # L1
    weekly_allowance = 10 # $10 a week
    allowance_fraction_saved_divisor = 2 # half of his allowance
    weekly_savings = weekly_allowance / allowance_fraction_saved_divisor

    # L2
    num_weeks = 8 # after 8 weeks
    total_savings_over_weeks = weekly_savings * num_weeks

    # L3
    initial_piggy_bank_amount = 43 # $43 in his piggy bank
    total_amount_in_piggy_bank = initial_piggy_bank_amount + total_savings_over_weeks

    # FA
    answer = total_amount_in_piggy_bank
    return answer