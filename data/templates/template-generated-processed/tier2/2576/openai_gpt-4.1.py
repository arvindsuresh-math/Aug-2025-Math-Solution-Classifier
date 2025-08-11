def solve():
    """Index: 2576.
    Returns: the net profit Brad earned from his lemonade stand.
    """
    # L1
    gallons_made = 2 # He made 2 gallons
    glasses_per_gallon = 16 # every gallon of lemonade would yield 16 glasses
    total_glasses = gallons_made * glasses_per_gallon

    # L2
    glasses_drank = 5 # He drank 5 glasses
    glasses_leftover = 6 # had 6 left over
    glasses_no_revenue = glasses_drank + glasses_leftover

    # L3
    glasses_sold = total_glasses - glasses_no_revenue

    # L4
    cost_per_gallon = 3.50 # cost him $3.50 to make every gallon
    total_cost = gallons_made * cost_per_gallon

    # L5
    price_per_glass = 1.00 # sell each glass for $1.00
    total_revenue = glasses_sold * price_per_glass

    # L6
    net_profit = total_revenue - total_cost

    # FA
    answer = net_profit
    return answer