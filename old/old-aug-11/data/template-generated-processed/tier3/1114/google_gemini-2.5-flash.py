def solve():
    """Index: 1114.
    Returns: the number of boxes Jeff can fill with his donuts.
    """
    # L1
    donuts_per_day = 10 # Jeff makes 10 donuts each day
    number_of_days = 12 # for 12 days
    total_donuts_made = donuts_per_day * number_of_days

    # L2
    donuts_jeff_eats_per_day = 1 # Jeff eats one of the donuts each day
    total_donuts_jeff_eats = donuts_jeff_eats_per_day * number_of_days

    # L3
    donuts_chris_eats = 8 # Chris then comes over and eats 8 donuts
    donuts_remaining_after_eating = total_donuts_made - total_donuts_jeff_eats - donuts_chris_eats

    # L4
    donuts_per_box = 10 # If 10 donuts fit in each box
    boxes_filled = donuts_remaining_after_eating / donuts_per_box

    # FA
    answer = boxes_filled
    return answer