def solve():
    """Index: 3693.
    Returns: the percentage of her life Wendy spent in an accounting-related job.
    """
    # L1
    years_as_accountant = 25 # 25 years as an accountant
    years_as_manager = 15 # 15 years as an accounting manager
    total_accounting_years = years_as_accountant + years_as_manager

    # L2
    total_life_years = 80 # lived to be 80 years old
    percentage_multiplier = 100 # WK
    percentage_of_life_in_accounting = (total_accounting_years / total_life_years) * percentage_multiplier

    # FA
    answer = percentage_of_life_in_accounting
    return answer