def solve():
    """Index: 211.
    Returns: how much more Jessica pays for her expenses over the whole year compared to last year.
    """
    # L1
    last_year_rent = 1000 # $1000 for rent each month
    rent_increase_percent = 0.3 # rent goes up by 30%
    rent_increase = last_year_rent * rent_increase_percent

    # L2
    last_year_food = 200 # $200 for food each month
    food_increase_percent = 0.5 # food costs increase by 50%
    food_increase = last_year_food * food_increase_percent

    # L3
    last_year_car_insurance = 100 # $100 for car insurance each month
    car_insurance_multiplier = 3 # cost of her car insurance triples
    new_car_insurance = last_year_car_insurance * car_insurance_multiplier

    # L4
    car_insurance_increase = new_car_insurance - last_year_car_insurance

    # L5
    monthly_total_increase = rent_increase + food_increase + car_insurance_increase

    # L6
    months_per_year = 12 # WK
    annual_increase = monthly_total_increase * months_per_year

    # FA
    answer = annual_increase
    return answer