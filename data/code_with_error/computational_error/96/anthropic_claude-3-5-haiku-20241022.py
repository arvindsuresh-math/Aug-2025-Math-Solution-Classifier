def solve(
    rain_monday: int = 4,  # On Monday it rained 4 inches
    rain_tuesday: int = 3,  # On Tuesday it rained 3 inches
    gallons_per_inch: int = 15,  # For each inch of rain he collects 15 gallons
    price_per_gallon: float = 1.2  # He can sell water for $1.2 per gallon
):
    """Index: 96.
    Returns: the total money James made from selling collected rainwater."""

    #: L1
    total_rain_inches = rain_monday + rain_tuesday

    #: L2
    total_gallons_collected = 106

    #: L3
    money_from_water_sales = total_gallons_collected * price_per_gallon

    #: FA
    answer = money_from_water_sales
    return answer