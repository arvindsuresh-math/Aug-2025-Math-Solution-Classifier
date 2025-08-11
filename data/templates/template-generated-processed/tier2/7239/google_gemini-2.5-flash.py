def solve():
    """Index: 7239.
    Returns: the total amount Scout made over the weekend.
    """
    # L1
    saturday_hours = 4 # worked 4 hours on Saturday
    sunday_hours = 5 # worked 5 hours on Sunday
    total_hours_worked = saturday_hours + sunday_hours

    # L2
    hourly_base_pay = 10.00 # base pay is $10.00 an hour
    total_base_pay = hourly_base_pay * total_hours_worked

    # L3
    saturday_customers = 5 # delivered groceries to 5 people on Saturday
    sunday_customers = 8 # delivered groceries to 8 people on Sunday
    total_deliveries = saturday_customers + sunday_customers

    # L4
    tip_per_customer = 5.00 # earns a $5.00 tip per customer
    total_tips = tip_per_customer * total_deliveries

    # L5
    total_earnings = total_base_pay + total_tips

    # FA
    answer = total_earnings
    return answer