def solve():
    """Index: 6266.
    Returns: the difference in raffle tickets sold on Saturday and Sunday.
    """
    # L1
    tickets_sold_friday = 181 # sold 181 raffle tickets
    multiplier_saturday = 2 # twice as many
    tickets_sold_saturday = tickets_sold_friday * multiplier_saturday

    # L2
    tickets_sold_sunday = 78 # sold 78 raffle tickets
    difference_saturday_sunday = tickets_sold_saturday - tickets_sold_sunday

    # FA
    answer = difference_saturday_sunday
    return answer