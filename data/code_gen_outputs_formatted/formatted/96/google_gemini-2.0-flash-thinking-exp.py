def solve(
    gallons_per_inch: int = 15, # For each inch of rain he collects 15 gallons
    rain_monday_inches: int = 4, # On Monday it rained 4 inches
    rain_tuesday_inches: int = 3, # on Tuesday it rained 3 inches
    price_per_gallon: float = 1.2 # He can sell water for $1.2 per gallon
):
    """Index: 96.
    Returns: the total money made from selling the collected rainwater.
    """

    #: L1
    total_rain_inches = rain_tuesday_inches + rain_monday_inches

    #: L2
    total_gallons_collected = total_rain_inches * gallons_per_inch

    #: L3
    total_money_made = total_gallons_collected * price_per_gallon

    answer = total_money_made # FINAL ANSWER
    return answer