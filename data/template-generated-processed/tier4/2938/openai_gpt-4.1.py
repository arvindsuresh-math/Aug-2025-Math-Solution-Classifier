def solve():
    """Index: 2938.
    Returns: the number of years Mike needs to save for the downpayment.
    """
    # L1
    salary = 150000 # $150,000 a year salary
    save_percent = 0.1 # puts away 10% of his salary
    annual_savings = salary * save_percent

    # L2
    house_cost = 450000 # $450,000 house
    downpayment_percent = 0.2 # needs to save up 20% of the cost
    downpayment_needed = house_cost * downpayment_percent

    # L3
    years_needed = downpayment_needed / annual_savings

    # FA
    answer = years_needed
    return answer