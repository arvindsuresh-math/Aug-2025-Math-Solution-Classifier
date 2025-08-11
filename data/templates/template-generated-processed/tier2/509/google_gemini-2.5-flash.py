def solve():
    """Index: 509.
    Returns: the total cost Coco will pay for using his oven.
    """
    # L1
    hours_used = 25 # 25 hours last month
    consumption_rate_per_hour = 2.4 # consumption rate of 2.4 kWh
    total_consumption_kW = hours_used * consumption_rate_per_hour

    # L2
    price_per_kW = 0.10 # $0.10 per kW
    total_cost = price_per_kW * total_consumption_kW

    # FA
    answer = total_cost
    return answer