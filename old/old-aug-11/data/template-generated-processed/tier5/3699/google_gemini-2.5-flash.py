def solve():
    """Index: 3699.
    Returns: the number of weeks until Carol and Mike have the same amount of money.
    """
    # L3
    carol_initial_money = 60 # Carol has $60
    carol_weekly_saving = 9 # saves $9 per week
    mike_initial_money = 90 # Mike has $90
    mike_weekly_saving = 3 # saves $3 per week
    initial_money_difference = mike_initial_money - carol_initial_money

    # L4
    weekly_saving_difference = carol_weekly_saving - mike_weekly_saving

    # L5
    num_weeks = initial_money_difference / weekly_saving_difference

    # FA
    answer = num_weeks
    return answer