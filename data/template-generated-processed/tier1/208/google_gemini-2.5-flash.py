def solve():
    """Index: 208.
    Returns: the amount of dollars left in the piggy bank.
    """
    # L1
    years_saved = 2 # 2 years
    months_per_year = 12 # WK
    total_months_saved = months_per_year * years_saved

    # L2
    monthly_deposit = 25 # $25 in his piggy bank every month
    total_saved_money = monthly_deposit * total_months_saved

    # L3
    spent_on_car_repair = 400 # $400 from his piggy bank savings
    money_left = total_saved_money - spent_on_car_repair

    # FA
    answer = money_left
    return answer