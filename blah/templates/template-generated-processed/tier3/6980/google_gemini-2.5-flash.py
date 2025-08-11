def solve():
    """Index: 6980.
    Returns: the number of donuts left in the box.
    """
    # L1
    initial_donuts = 50 # box of donuts that has 50 in total
    eaten_by_bill = 2 # He eats 2 on the ride in
    donuts_after_bill_eats = initial_donuts - eaten_by_bill

    # L2
    taken_by_secretary = 4 # the secretary takes another 4
    donuts_after_secretary_takes = donuts_after_bill_eats - taken_by_secretary

    # L3
    coworker_divisor = 2 # steal half the remaining donuts
    donuts_remaining_after_coworkers = donuts_after_secretary_takes / coworker_divisor

    # FA
    answer = donuts_remaining_after_coworkers
    return answer