def solve():
    """Index: 4533.
    Returns: the profit Mike made from the land development.
    """
    # L1
    total_acres = 200 # 200 acres
    cost_per_acre = 70 # $70 per acre
    total_cost_of_land = total_acres * cost_per_acre

    # L2
    sold_fraction_denominator = 2 # half of the acreage
    acres_sold = total_acres / sold_fraction_denominator

    # L3
    sale_price_per_acre = 200 # $200 per acre
    total_revenue_from_sale = acres_sold * sale_price_per_acre

    # L4
    profit = total_revenue_from_sale - total_cost_of_land

    # FA
    answer = profit
    return answer