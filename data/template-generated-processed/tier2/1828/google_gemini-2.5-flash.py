def solve():
    """Index: 1828.
    Returns: the total money Joseph will have in the fund after two years.
    """
    # L1
    initial_investment = 1000 # invested $1000
    monthly_deposit = 100 # deposited an additional $100 every month
    months_per_year = 12 # WK
    total_invested_year1 = initial_investment + (monthly_deposit * months_per_year)

    # L2
    yearly_interest_rate_percent = 10 # yearly interest rate of 10%
    percent_factor = 0.01 # WK
    interest_year1 = total_invested_year1 * yearly_interest_rate_percent * percent_factor

    # L3
    value_after_year1 = total_invested_year1 + interest_year1

    # L4
    total_invested_year2 = value_after_year1 + (monthly_deposit * months_per_year)

    # L5
    interest_year2 = total_invested_year2 * yearly_interest_rate_percent * percent_factor

    # L6
    final_investment_value = total_invested_year2 + interest_year2

    # FA
    answer = final_investment_value
    return answer