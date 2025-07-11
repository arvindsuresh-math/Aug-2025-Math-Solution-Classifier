def solve():
    """Index: 1396.
    Returns: Mrs. Lim's total revenue for the milk.
    """
    # L1
    yesterday_morning_milk = 68 # got 68 gallons of milk
    fewer_gallons_this_morning = 18 # 18 gallons fewer
    this_morning_milk = yesterday_morning_milk - fewer_gallons_this_morning

    # L2
    yesterday_evening_milk = 82 # in the evening, she got 82 gallons
    total_milk_produced = yesterday_morning_milk + yesterday_evening_milk + this_morning_milk

    # L3
    gallons_left = 24 # has only 24 gallons left
    gallons_sold = total_milk_produced - gallons_left

    # L4
    cost_per_gallon = 3.50 # each gallon costs $3.50
    total_revenue = cost_per_gallon * gallons_sold

    # FA
    answer = total_revenue
    return answer