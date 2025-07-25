def solve_46():
    # Piano practice time per day
    piano_practice_per_day = 20

    # Violin practice time per day is three times the piano practice time
    violin_practice_per_day = piano_practice_per_day * 3

    # Total practice time per day (piano + violin)
    total_practice_per_day = piano_practice_per_day + violin_practice_per_day

    # Number of practice days per week
    practice_days_per_week = 6

    # Total practice time per week
    total_practice_per_week = total_practice_per_day * practice_days_per_week

    # Number of weeks in a month
    weeks_in_month = 4

    # Total practice time per month
    total_practice_per_month = total_practice_per_week * weeks_in_month

    return total_practice_per_month