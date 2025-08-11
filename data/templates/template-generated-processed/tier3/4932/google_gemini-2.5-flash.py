def solve():
    """Index: 4932.
    Returns: the total money made by the theater on Friday night.
    """
    # L1
    matinee_ticket_price = 5 # $5 for matinee tickets
    matinee_customers = 32 # 32 matinee customers
    matinee_revenue = matinee_ticket_price * matinee_customers

    # L2
    evening_ticket_price = 7 # $7 for evening tickets
    evening_customers = 40 # 40 evening customers
    evening_revenue = evening_ticket_price * evening_customers

    # L3
    opening_night_ticket_price = 10 # $10 for opening night tickets
    opening_night_customers = 58 # 58 customers for an opening night showing
    opening_night_revenue = opening_night_ticket_price * opening_night_customers

    # L4
    total_customers = matinee_customers + evening_customers + opening_night_customers

    # L5
    popcorn_customer_divisor = 2 # half the customers bought popcorn
    popcorn_customers = total_customers / popcorn_customer_divisor

    # L6
    popcorn_cost = 10 # A bucket of popcorn costs $10
    popcorn_revenue = popcorn_cost * popcorn_customers

    # L7
    total_revenue = matinee_revenue + evening_revenue + opening_night_revenue + popcorn_revenue

    # FA
    answer = total_revenue
    return answer