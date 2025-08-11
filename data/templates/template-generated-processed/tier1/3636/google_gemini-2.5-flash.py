def solve():
    """Index: 3636.
    Returns: the amount of money Janet needed to rent the apartment.
    """
    # L1
    num_months_advance = 2 # 2 months' rent in advance
    monthly_rent = 1250 # $1,250 per month
    advance_rent_cost = num_months_advance * monthly_rent

    # L2
    deposit_amount = 500 # deposit of $500
    total_cost_to_rent = advance_rent_cost + deposit_amount

    # L3
    money_saved = 2225 # $2,225 saved
    money_needed = total_cost_to_rent - money_saved

    # FA
    answer = money_needed
    return answer