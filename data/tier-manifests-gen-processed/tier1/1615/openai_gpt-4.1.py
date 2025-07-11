def solve():
    """Index: 1615.
    Returns: the total amount Elias spends on bars of soap in two years.
    """
    # L1
    cost_per_bar = 4 # each bar of soap costs $4
    months_per_year = 12 # WK
    yearly_soap_cost = cost_per_bar * months_per_year

    # L2
    years = 2 # in two years
    total_cost = years * yearly_soap_cost

    # FA
    answer = total_cost
    return answer