def solve():
    """Index: 2938.
    Returns: the number of years it will take to save for the downpayment.
    """
    # L1
    salary_per_year = 150000 # $150,000 a year salary
    savings_rate = 0.1 # 10% of his ... salary
    annual_savings = salary_per_year * savings_rate

    # L2
    house_cost = 450000 # $450,000 house
    downpayment_percentage = 0.2 # 20% of the cost
    required_downpayment = house_cost * downpayment_percentage

    # L3
    years_to_save = required_downpayment / annual_savings

    # FA
    answer = years_to_save
    return answer