def solve(
        gallons_per_inch: int = 15, # For each inch of rain he collects 15 gallons
        rain_monday_inches: int = 4, # On Monday it rained 4 inches
        rain_tuesday_inches: int = 3, # and on Tuesday it rained 3 inches
        price_per_gallon: float = 1.2 # He can sell water for $1.2 per gallon
    ):
    """Index: 96.
    Returns: the total money James made from selling all the collected water.
    """

    #: L1
    total_inches_rain = rain_tuesday_inches + rain_monday_inches # eval: 7 = 3 + 4

    #: L2
    total_gallons_collected = total_inches_rain * gallons_per_inch # eval: 105 = 7 * 15

    #: L3
    money_made = total_gallons_collected * gallons_per_inch # eval: 1575 = 105 * 15

    #: FA
    answer = money_made
    return answer # eval: return 1575
