def solve():
    """Index: 509.
    Returns: the total amount Coco will pay for using his oven for 25 hours last month.
    """
    # L1
    usage_hours = 25 # used it for a total of 25 hours last month
    consumption_per_hour = 2.4 # consumption rate of 2.4 kWh (kilowatt-hours)
    total_consumption = usage_hours * consumption_per_hour

    # L2
    price_per_kw = 0.10 # electricity price is $0.10 per kW
    total_cost = price_per_kw * total_consumption

    # FA
    answer = total_cost
    return answer