def solve():
    """Index: 4203.
    Returns: the amount left for gas and maintenance after buying a car.
    """
    # L1
    rent_cost = 1250 # $1250 for rent
    utilities_cost = 150 # $150 on utilities
    retirement_savings_cost = 400 # $400 into retirement & savings accounts
    groceries_cost = 300 # $300.00 on groceries/eating out
    insurance_cost = 200 # $200 for insurance
    miscellaneous_cost = 200 # $200 for miscellaneous expenses
    total_monthly_bills = rent_cost + utilities_cost + retirement_savings_cost + groceries_cost + insurance_cost + miscellaneous_cost

    # L2
    monthly_income = 3200 # $3200.00 every month
    remaining_after_bills = monthly_income - total_monthly_bills

    # L3
    car_payment = 350 # monthly car payment of $350
    left_for_gas_maintenance = remaining_after_bills - car_payment

    # FA
    answer = left_for_gas_maintenance
    return answer