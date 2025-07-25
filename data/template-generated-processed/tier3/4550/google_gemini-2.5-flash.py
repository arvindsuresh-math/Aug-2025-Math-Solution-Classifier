def solve():
    """Index: 4550.
    Returns: the total kilograms of cabbage sold.
    """
    # L1
    wednesday_earnings = 30 # $30 last Wednesday
    price_per_kg = 2 # $2 per kilogram
    kg_sold_wednesday = wednesday_earnings / price_per_kg

    # L2
    friday_earnings = 24 # $24 last Friday
    kg_sold_friday = friday_earnings / price_per_kg

    # L3
    today_earnings = 42 # $42 today
    kg_sold_today = today_earnings / price_per_kg

    # L4
    total_kg_sold = kg_sold_wednesday + kg_sold_friday + kg_sold_today

    # FA
    answer = total_kg_sold
    return answer