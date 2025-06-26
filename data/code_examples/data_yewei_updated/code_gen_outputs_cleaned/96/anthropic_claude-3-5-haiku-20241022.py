def solve(
    gallons_per_inch: int = 15,  # For each inch of rain he collects 15 gallons
    monday_rain: int = 4,  # On Monday it rained 4 inches
    tuesday_rain: int = 3,  # On Tuesday it rained 3 inches
    price_per_gallon: float = 1.2  # He can sell water for $1.2 per gallon
):
    """Index: 96.
    Returns: the total money made from selling collected rainwater."""
    #: L1
    total_rain_inches = monday_rain + tuesday_rain

    #: L2
    total_gallons_collected = total_rain_inches * gallons_per_inch

    #: L3
    money_from_water_sales = total_gallons_collected * price_per_gallon

    answer = money_from_water_sales  # FINAL ANSWER
    return answer