def solve():
    """Index: 5941.
    Returns: the number of gallons of milk Aunt May has left.
    """
    # L1
    morning_milk = 365 # This morning she got 365 gallons of milk
    evening_milk = 380 # This evening she got 380 gallons
    total_milk_today = morning_milk + evening_milk

    # L2
    sold_to_factory = 612 # sold 612 gallons to the local ice cream factory
    milk_after_sale = total_milk_today - sold_to_factory

    # L3
    leftover_yesterday = 15 # 15 gallons left over from yesterday
    final_milk_left = milk_after_sale + leftover_yesterday

    # FA
    answer = final_milk_left
    return answer