def solve(
    rain_monday: int = 4,  # On Monday it rained 4 inches
    rain_tuesday: int = 3,  # on Tuesday it rained 3 inches
    gallons_per_inch: int = 15,  # For each inch of rain he collects 15 gallons
    price_per_gallon: float = 1.2  # He can sell water for $1.2 per gallon
):
    """Index: 96.
    Returns: the total money made from selling all the collected water.
    """

    #: L1
    total_rain_inches = rain_monday + rain_tuesday # eval: 7 = 4 + 3

    #: L2
    total_gallons_collected = total_rain_inches * gallons_per_inch # eval: 105 = 7 * 15

    #: L3
    total_money_made = total_gallons_collected + price_per_gallon # eval: 106.2 = 105 + 1.2

    #: FA
    answer = total_money_made
    return answer # eval: return 106.2
