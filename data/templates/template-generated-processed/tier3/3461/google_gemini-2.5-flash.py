def solve():
    """Index: 3461.
    Returns: the number of days the meat supply will last.
    """
    # L1
    lion_consumption = 25 # lion consumes 25 kilograms of meat
    tiger_consumption = 20 # tiger consumes 20 kilograms of meat
    total_daily_consumption = lion_consumption + tiger_consumption

    # L2
    total_meat_supply = 90 # they have 90 kilograms of meat
    days_meat_will_last = total_meat_supply / total_daily_consumption

    # FA
    answer = days_meat_will_last
    return answer