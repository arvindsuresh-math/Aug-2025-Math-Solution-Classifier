def solve(
    gallons_per_inch: int = 15, # For each inch of rain he collects 15 gallons
    inches_monday: int = 4, # On Monday it rained 4 inches
    inches_tuesday: int = 3, # on Tuesday it rained 3 inches
    price_per_gallon: float = 1.2 # He can sell water for $1.2 per gallon
):
    """Index: 96.
    Returns: the total amount of money James made from selling all the water.
    """
    #: L1
    total_inches_rain = inches_monday + inches_tuesday

    #: L2
    total_gallons_collected = total_inches_rain * gallons_per_inch

    #: L3
    total_money_made = total_gallons_collected * price_per_gallon

    answer = total_money_made # FINAL ANSWER
    return answer