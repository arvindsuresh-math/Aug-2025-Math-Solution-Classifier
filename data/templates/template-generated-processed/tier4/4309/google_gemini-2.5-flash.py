def solve():
    """Index: 4309.
    Returns: the total cost Mark needs to pay for asphalt, including tax.
    """
    # L1
    road_length = 2000 # 2000 feet long
    road_width = 20 # 20 feet wide
    area_to_cover = road_length * road_width

    # L2
    sqft_per_truckload = 800 # 800 square feet of road
    num_truckloads = area_to_cover / sqft_per_truckload

    # L3
    cost_per_truckload = 75 # $75
    cost_before_tax = cost_per_truckload * num_truckloads

    # L4
    sales_tax_percent = 0.2 # 20% sales tax
    sales_tax_amount = cost_before_tax * sales_tax_percent

    # L5
    total_cost = sales_tax_amount + cost_before_tax

    # FA
    answer = total_cost
    return answer