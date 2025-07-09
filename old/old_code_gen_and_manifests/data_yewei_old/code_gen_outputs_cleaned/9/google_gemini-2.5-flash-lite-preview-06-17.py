# Tina's hourly wage
hourly_wage = 18.00

# Number of hours worked per day
hours_per_day = 10

# Number of days worked
days_worked = 5

# Regular hours per shift
regular_hours_per_shift = 8

# Calculate regular pay per day
regular_pay_per_day = regular_hours_per_shift * hourly_wage

# Calculate overtime hours per day
overtime_hours_per_day = hours_per_day - regular_hours_per_shift

# Calculate overtime hourly rate
overtime_rate = hourly_wage + (hourly_wage * 0.5)

# Calculate overtime pay per day
overtime_pay_per_day = overtime_hours_per_day * overtime_rate

# Calculate total pay per day
total_pay_per_day = regular_pay_per_day + overtime_pay_per_day

# Calculate total earnings for the week
total_earnings = total_pay_per_day * days_worked

print(f"Tina makes ${total_earnings:.2f}")