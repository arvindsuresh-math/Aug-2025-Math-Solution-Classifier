def solve():
    """Index: 1828.
    Returns: the total amount Joseph will have in the fund after two years.
    """
    # L1
    initial_investment = 1000 # Joseph invested $1000
    monthly_deposit = 100 # $100 every month
    months_per_year = 12 # WK
    first_year_total_invested = initial_investment + monthly_deposit * months_per_year

    # L2
    interest_rate_percent = 10 # yearly interest rate of 10%
    percent_factor = 0.01 # WK
    first_year_interest = first_year_total_invested * interest_rate_percent * percent_factor

    # L3
    first_year_total_value = first_year_total_invested + first_year_interest

    # L4
    second_year_total_invested = first_year_total_value + monthly_deposit * months_per_year

    # L5
    second_year_interest = second_year_total_invested * interest_rate_percent * percent_factor

    # L6
    total_after_two_years = second_year_total_invested + second_year_interest

    # FA
    answer = total_after_two_years
    return answer