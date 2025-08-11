def solve():
    """Index: 3679.
    Returns: the number of weeks Macey needs to save.
    """
    # L1
    shirt_cost = 3.0 # shirt that costs $3
    saved_already = 1.50 # save $1.50 already
    remaining_amount = shirt_cost - saved_already

    # L2
    savings_per_week = 0.50 # saves $0.50 per week
    weeks_needed = remaining_amount / savings_per_week

    # FA
    answer = weeks_needed
    return answer