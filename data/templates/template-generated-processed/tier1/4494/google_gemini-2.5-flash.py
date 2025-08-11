def solve():
    """Index: 4494.
    Returns: how much more money Thomas needs to buy the car by the end of the 2 years.
    """
    # L1
    weeks_per_year = 52 # WK

    # L2
    weekly_allowance_year1 = 50 # weekly allowance was $50
    allowance_year1_total = weeks_per_year * weekly_allowance_year1

    # L3
    hourly_wage = 9 # pays $9 an hour
    hours_per_week = 30 # worked 30 hours a week
    earned_per_week_year2 = hourly_wage * hours_per_week

    # L4
    earned_year2_total = weeks_per_year * earned_per_week_year2

    # L5
    total_earned_two_years = earned_year2_total + allowance_year1_total

    # L6
    weekly_expenses = 35 # spends $35 a week on himself
    num_years = 2 # by the end of the 2 years
    total_weeks_two_years = weeks_per_year * num_years
    total_expenses_two_years = weekly_expenses * total_weeks_two_years

    # L7
    total_saved = total_earned_two_years - total_expenses_two_years

    # L8
    car_cost = 15000 # car he wants to buy is $15,000
    money_needed = car_cost - total_saved

    # FA
    answer = money_needed
    return answer