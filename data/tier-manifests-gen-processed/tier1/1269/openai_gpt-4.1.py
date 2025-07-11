def solve():
    """Index: 1269.
    Returns: the total revenue for the day at the Kwik-e-Tax Center.
    """
    # L1
    federal_price = 50 # $50 for a federal return
    num_federal = 60 # sell 60 federal returns
    federal_income = federal_price * num_federal

    # L2
    state_price = 30 # $30 for a state return
    num_state = 20 # sell 20 state returns
    state_income = state_price * num_state

    # L3
    quarterly_price = 80 # $80 for quarterly business taxes
    num_quarterly = 10 # sell 10 quarterly returns
    quarterly_income = quarterly_price * num_quarterly

    # L4
    total_income = federal_income + state_income + quarterly_income

    # FA
    answer = total_income
    return answer