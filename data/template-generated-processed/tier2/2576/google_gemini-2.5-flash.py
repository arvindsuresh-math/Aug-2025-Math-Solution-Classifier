def solve():
    """Index: 2576.
    Returns: the net profit Brad earned.
    """
    # L1
    gallons_made = 2 # He made 2 gallons
    glasses_per_gallon = 16 # Every gallon of lemonade would yield 16 glasses
    total_glasses_made = gallons_made * glasses_per_gallon

    # L2
    glasses_drank = 5 # He drank 5 glasses
    glasses_left_over = 6 # sold all but 6 glasses of lemonade
    glasses_not_sold = glasses_drank + glasses_left_over

    # L3
    glasses_sold = total_glasses_made - glasses_not_sold

    # L4
    cost_per_gallon = 3.50 # cost him $3.50 to make every gallon of lemonade
    total_cost = gallons_made * cost_per_gallon

    # L5
    price_per_glass = 1.00 # sell each glass for $1.00
    total_revenue = price_per_glass * glasses_sold

    # L6
    net_profit = total_revenue - total_cost

    # FA
    answer = net_profit
    return answer