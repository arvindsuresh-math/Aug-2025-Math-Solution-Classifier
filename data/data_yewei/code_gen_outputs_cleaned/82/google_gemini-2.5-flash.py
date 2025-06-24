def solve_82():
    # Base weekly hours and income
    base_hours = 40
    base_income = 500

    # Hours worked last week
    hours_worked = 50

    # Calculate overtime hours
    overtime_hours = hours_worked - base_hours

    # Overtime rate per hour
    overtime_rate = 20

    # Calculate overtime pay
    overtime_pay = overtime_hours * overtime_rate

    # Calculate total income
    total_income = base_income + overtime_pay

    return total_income

# Execute the function to get the answer
# print(solve_82())