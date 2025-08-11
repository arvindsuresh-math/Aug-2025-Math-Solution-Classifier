def solve():
    """Index: 427.
    Returns: the total amount of money in Sheila's piggy bank at the end of 4 years.
    """
    # L1
    initial_savings = 3000 # saved $3,000
    family_addition = 7000 # secretly added $7,000
    current_total = initial_savings + family_addition

    # L2
    months_per_year = 12 # WK
    saving_years = 4 # for 4 years
    total_months = months_per_year * saving_years

    # L3
    monthly_saving = 276 # saving $276 per month
    savings_over_time = monthly_saving * total_months

    # L4
    final_total = current_total + savings_over_time

    # FA
    answer = final_total
    return answer