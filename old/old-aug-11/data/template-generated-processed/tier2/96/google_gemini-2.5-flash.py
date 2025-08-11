def solve():
    """Index: 96.
    Returns: the total money made from selling the water.
    """
    # L1
    rain_tuesday = 3 # on Tuesday it rained 3 inches
    rain_monday = 4 # On Monday it rained 4 inches
    total_rain_inches = rain_tuesday + rain_monday

    # L2
    gallons_per_inch = 15 # For each inch of rain he collects 15 gallons
    total_gallons = total_rain_inches * gallons_per_inch

    # L3
    price_per_gallon = 1.2 # sell water for $1.2 per gallon
    total_money_made = total_gallons * price_per_gallon

    # FA
    answer = total_money_made
    return answer