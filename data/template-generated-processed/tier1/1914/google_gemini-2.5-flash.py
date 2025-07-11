def solve():
    """Index: 1914.
    Returns: the total amount Darla pays.
    """
    # L1
    cost_per_watt = 4 # $4/watt of electricity
    watts_needed = 300 # 300 watts of electricity
    electricity_cost = cost_per_watt * watts_needed

    # L2
    late_fee = 150 # $150 late fee
    total_payment = electricity_cost + late_fee

    # FA
    answer = total_payment
    return answer