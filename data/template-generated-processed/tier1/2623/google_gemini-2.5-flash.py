def solve():
    """Index: 2623.
    Returns: the number of additional blue tickets Tom needs to win a new Bible.
    """
    # L1
    blue_tickets_per_red_ticket = 10 # each red ticket is obtained by trading in 10 blue tickets
    red_tickets_per_yellow_ticket = 10 # each yellow ticket is obtained by trading in 10 red tickets
    blue_tickets_per_yellow_ticket = red_tickets_per_yellow_ticket * blue_tickets_per_red_ticket

    # L2
    yellow_tickets_for_bible = 10 # 10 yellow tickets to win a brand new Bible
    total_blue_tickets_needed = yellow_tickets_for_bible * blue_tickets_per_yellow_ticket

    # L3
    tom_yellow_tickets = 8 # 8 yellow tickets
    tom_yellow_tickets_in_blue = tom_yellow_tickets * blue_tickets_per_yellow_ticket

    # L4
    tom_red_tickets = 3 # 3 red tickets
    tom_red_tickets_in_blue = tom_red_tickets * blue_tickets_per_red_ticket

    # L5
    tom_blue_tickets = 7 # 7 blue tickets
    tom_total_blue_tickets = tom_yellow_tickets_in_blue + tom_red_tickets_in_blue + tom_blue_tickets

    # L6
    blue_tickets_needed_more = total_blue_tickets_needed - tom_total_blue_tickets

    # FA
    answer = blue_tickets_needed_more
    return answer