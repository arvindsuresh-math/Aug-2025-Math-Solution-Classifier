def solve():
    """Index: 3510.
    Returns: the amount Alfred needs to save each month.
    """
    # L1
    total_goal_amount = 1000.00 # Alfred likes to save $1,000.00
    left_over_amount = 100.00 # He has $100.00 left over from last year's holiday
    money_needed_to_save = total_goal_amount - left_over_amount

    # L2
    num_months = 12 # over 12 months
    monthly_saving_needed = money_needed_to_save / num_months

    # FA
    answer = monthly_saving_needed
    return answer