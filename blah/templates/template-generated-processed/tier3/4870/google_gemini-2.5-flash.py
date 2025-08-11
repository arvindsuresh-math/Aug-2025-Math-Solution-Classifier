def solve():
    """Index: 4870.
    Returns: the total revenue of the concert.
    """
    # L1
    num_adults = 183 # 183 adults
    adult_ticket_price = 26 # ticket price for adults is $26
    revenue_adults = num_adults * adult_ticket_price

    # L2
    child_price_divisor = 2 # for children, the price is half
    child_ticket_price = adult_ticket_price / child_price_divisor

    # L3
    num_children = 28 # 28 children who attended
    revenue_children = num_children * child_ticket_price

    # L4
    total_revenue = revenue_adults + revenue_children

    # FA
    answer = total_revenue
    return answer