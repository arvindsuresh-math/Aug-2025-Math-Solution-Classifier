def solve():
    """Index: 7032.
    Returns: the number of donuts left for co-workers.
    """
    # L1
    donuts_dozen_quantity = 2.5 # 2 and a half dozen donuts
    donuts_per_dozen = 12 # WK
    total_donuts_bought = donuts_dozen_quantity * donuts_per_dozen

    # L2
    eaten_percent_decimal = 0.10 # from solution text: .10*30
    eaten_percent_num = 10 # 10% of the donuts
    percent_factor = 0.01 # WK
    donuts_eaten_driving = eaten_percent_num * percent_factor * total_donuts_bought

    # L3
    donuts_after_driving = total_donuts_bought - donuts_eaten_driving

    # L4
    donuts_taken_snack = 4 # grabs another 4 donuts
    donuts_left_for_coworkers = donuts_after_driving - donuts_taken_snack

    # FA
    answer = donuts_left_for_coworkers
    return answer