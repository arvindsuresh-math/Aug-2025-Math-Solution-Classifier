def solve():
    # Given values
    hourly_wage = 18.00
    regular_hours_per_shift = 8
    total_hours_per_day = 10
    num_days_worked = 5

    # L1: Calculate regular pay for an 8-hour shift
    regular_daily_pay = regular_hours_per_shift * hourly_wage

    # L2: Calculate overtime hours per day
    overtime_hours_per_day = total_hours_per_day - regular_hours_per_shift

    # L3: Calculate the extra amount for overtime pay (1/2 of hourly wage)
    overtime_extra_per_hour = hourly_wage * 0.5

    # L4: Calculate the full overtime hourly rate
    overtime_hourly_rate = hourly_wage + overtime_extra_per_hour

    # L5: Calculate total regular pay for 5 days
    total_regular_pay_5_days = regular_daily_pay * num_days_worked

    # L6: Calculate total overtime pay for one day
    overtime_daily_pay = overtime_hours_per_day * overtime_hourly_rate

    # L7: Calculate total overtime pay for 5 days
    total_overtime_pay_5_days = overtime_daily_pay * num_days_worked

    # L8: Calculate total earnings for 5 days
    total_earnings = total_regular_pay_5_days + total_overtime_pay_5_days

    return total_earnings

# Execute the function to get the answer
answer = solve()