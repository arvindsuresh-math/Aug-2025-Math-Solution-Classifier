def solve():
    """Index: 1935.
    Returns: the original amount of money Reese had in her savings account.
    """
    # L1
    february_percentage = 20 # spent 20% of her savings for her expenses in February
    march_percentage = 40 # 40% of it in March
    total_percentage_spent_feb_mar = february_percentage + march_percentage

    # L2
    total_percentage_base = 100 # WK
    remaining_percentage = total_percentage_base - total_percentage_spent_feb_mar

    # L3
    money_left = 2900 # she still has $2900
    april_expenses = 1500 # and $1500 in April
    amount_corresponding_to_remaining_percentage = money_left + april_expenses

    # L4
    value_per_percent = amount_corresponding_to_remaining_percentage / remaining_percentage

    # L5
    original_savings = value_per_percent * total_percentage_base

    # FA
    answer = original_savings
    return answer