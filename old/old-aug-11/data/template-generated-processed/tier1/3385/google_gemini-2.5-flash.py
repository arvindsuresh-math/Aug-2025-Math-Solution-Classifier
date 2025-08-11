def solve():
    """Index: 3385.
    Returns: the amount Daria still owes before interest.
    """
    # L1
    couch_cost = 750 # a couch for $750
    table_cost = 100 # a table for $100
    lamp_cost = 50 # a lamp for $50
    total_furniture_cost = couch_cost + table_cost + lamp_cost

    # L2
    initial_payment = 500 # $500 saved ready to pay
    amount_owed_before_interest = total_furniture_cost - initial_payment

    # FA
    answer = amount_owed_before_interest
    return answer