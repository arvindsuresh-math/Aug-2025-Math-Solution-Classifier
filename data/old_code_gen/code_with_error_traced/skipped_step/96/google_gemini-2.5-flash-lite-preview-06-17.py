def solve(
    gallons_per_inch: int = 15, # For each inch of rain he collects 15 gallons
    inches_monday: int = 4, # On Monday it rained 4 inches
    inches_tuesday: int = 3, # and on Tuesday it rained 3 inches
    price_per_gallon: float = 1.2 # He can sell water for $1.2 per gallon
):
    """Index: 96.
    Returns: the total amount of money James made from selling all the water.
    """

    #: L1

    #: L2
    total_gallons_collected = price_per_gallon * gallons_per_inch # eval: 18.0 = 1.2 * 15

    #: L3
    total_money_made = total_gallons_collected * price_per_gallon # eval: 21.599999999999998 = 18.0 * 1.2

    #: FA
    answer = total_money_made
    return answer # eval: return 21.599999999999998
