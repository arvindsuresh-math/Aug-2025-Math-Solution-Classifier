def solve():
    """Index: 1539.
    Returns: the difference between the amounts Chris will earn from the two offers.
    """
    # L1
    asking_price = 5200 # Chris is trying to sell his car for $5200
    maintenance_inspection_divisor = 10 # a tenth of Chris’s asking price
    maintenance_inspection_cost = asking_price / maintenance_inspection_divisor
    earnings_first_buyer = asking_price - maintenance_inspection_cost

    # L2
    headlight_cost = 80 # replaced the headlights for $80
    tire_cost_multiplier = 3 # the tires for three times as much
    total_multiplier = 1 + tire_cost_multiplier # WK
    total_repair_cost = headlight_cost * total_multiplier
    earnings_second_buyer = asking_price - headlight_cost - (headlight_cost * tire_cost_multiplier)

    # L3
    difference_in_earnings = earnings_second_buyer - earnings_first_buyer

    # FA
    answer = difference_in_earnings
    return answer