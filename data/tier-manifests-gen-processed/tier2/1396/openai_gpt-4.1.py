def solve():
    """Index: 1396.
    Returns: Mrs. Lim's total revenue for the milk sold.
    """
    # L1
    yesterday_morning_gallons = 68 # 68 gallons of milk yesterday morning
    fewer_gallons = 18 # 18 gallons fewer than she had yesterday morning
    this_morning_gallons = yesterday_morning_gallons - fewer_gallons

    # L2
    yesterday_evening_gallons = 82 # 82 gallons in the evening
    total_gallons = yesterday_morning_gallons + yesterday_evening_gallons + this_morning_gallons

    # L3
    gallons_left = 24 # only 24 gallons left
    gallons_sold = total_gallons - gallons_left

    # L4
    price_per_gallon = 3.50 # each gallon costs $3.50
    revenue = price_per_gallon * gallons_sold

    # FA
    answer = revenue
    return answer