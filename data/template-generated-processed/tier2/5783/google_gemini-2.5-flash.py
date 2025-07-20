def solve():
    """Index: 5783.
    Returns: the total amount of money the three children save together.
    """
    # L1
    josiah_daily_saving = 0.25 # a quarter
    josiah_days = 24 # 24 days
    josiah_total_saving = josiah_daily_saving * josiah_days

    # L2
    leah_daily_saving = 0.50 # 50 cents
    leah_days = 20 # 20 days
    leah_total_saving = leah_daily_saving * leah_days

    # L3
    megan_daily_saving = 1 # twice as much as Leah (0.50 * 2 = 1)
    megan_days = 12 # 12 days
    megan_total_saving = megan_daily_saving * megan_days

    # L4
    total_saving = josiah_total_saving + leah_total_saving + megan_total_saving

    # FA
    answer = total_saving
    return answer