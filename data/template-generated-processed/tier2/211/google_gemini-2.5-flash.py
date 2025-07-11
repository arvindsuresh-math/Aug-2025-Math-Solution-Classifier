def solve():
    """Index: 211.
    Returns: the annual increase in Jessica's expenses.
    """
    # L1
    last_year_rent = 1000 # $1000 for rent
    rent_increase_percent_decimal = 0.3 # rent goes up by 30%
    rent_increase_amount = last_year_rent * rent_increase_percent_decimal

    # L2
    last_year_food_cost = 200 # $200 for food
    food_increase_percent_decimal = 0.5 # food costs increase by 50%
    food_increase_amount = last_year_food_cost * food_increase_percent_decimal

    # L3
    last_year_car_insurance = 100 # $100 for car insurance
    insurance_increase_factor = 3 # car insurance triples
    new_car_insurance_cost = last_year_car_insurance * insurance_increase_factor

    # L4
    car_insurance_increase_amount = new_car_insurance_cost - last_year_car_insurance

    # L5
    total_monthly_increase = rent_increase_amount + food_increase_amount + car_insurance_increase_amount

    # L6
    months_per_year = 12 # WK
    annual_increase = total_monthly_increase * months_per_year

    # FA
    answer = annual_increase
    return answer