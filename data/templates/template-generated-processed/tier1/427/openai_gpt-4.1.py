def solve():
    """Index: 427.
    Returns: the total amount of money in Sheila's piggy bank at the end of 4 years.
    """
    # L1
    sheila_saved = 3000 # she had saved $3,000
    family_added = 7000 # family secretly added $7,000
    initial_total = sheila_saved + family_added

    # L2
    months_per_year = 12 # WK
    years = 4 # for 4 years
    total_months = months_per_year * years

    # L3
    monthly_saving = 276 # saving $276 per month
    sheila_future_saving = monthly_saving * total_months

    # L4
    final_total = initial_total + sheila_future_saving

    # FA
    answer = final_total
    return answer