def solve():
    """Index: 2788.
    Returns: the amount of money Dr. Jones has left after paying his bills.
    """
    # L1
    monthly_earning = 6000 # Dr. Jones earns $6,000 a month
    electric_water_divisor = 4 # 1/4 of what he makes
    electric_water_bill = monthly_earning / electric_water_divisor

    # L2
    insurance_divisor = 5 # 1/5 of what he makes
    insurance_cost = monthly_earning / insurance_divisor

    # L3
    total_bills_insurances = electric_water_bill + insurance_cost

    # L4
    remaining_after_bills_insurances = monthly_earning - total_bills_insurances

    # L5
    house_rental = 640 # His house rental is $640 each month
    food_expense = 380 # his monthly food expense is $380
    total_rent_food = house_rental + food_expense

    # L6
    money_left = remaining_after_bills_insurances - total_rent_food

    # FA
    answer = money_left
    return answer