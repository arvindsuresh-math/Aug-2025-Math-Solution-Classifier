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
    total_rain_inches = rain_tuesday_inches + rain_monday_inches # eval: 7 = 3 + 4

    #: L2

    #: L3
    total_money_made = price_per_gallon * price_per_gallon # eval: 1.44 = 1.2 * 1.2

    #: FA
    answer = total_money_made
    return answer # eval: return 1.44
