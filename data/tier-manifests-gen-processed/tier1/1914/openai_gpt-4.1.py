def solve():
    """Index: 1914.
    Returns: the total amount Darla pays including electricity and late fee.
    """
    # L1
    cost_per_watt = 4 # $4/watt of electricity
    num_watts = 300 # 300 watts of electricity
    electricity_cost = cost_per_watt * num_watts

    # L2
    late_fee = 150 # $150 late fee
    total_cost = electricity_cost + late_fee

    # FA
    answer = total_cost
    return answer