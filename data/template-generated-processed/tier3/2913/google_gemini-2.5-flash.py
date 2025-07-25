def solve():
    """Index: 2913.
    Returns: the number of tickets that still need to be sold.
    """
    # L1
    jude_tickets = 16 # Jude sold 16 tickets
    andrea_multiplier = 2 # twice as many tickets as Jude
    andrea_tickets = jude_tickets * andrea_multiplier

    # L2
    half_divisor = 2 # half the number of tickets Jude sold
    half_jude_tickets = jude_tickets / half_divisor

    # L3
    sandra_adder = 4 # 4 more than half the number of tickets Jude sold
    sandra_tickets = half_jude_tickets + sandra_adder

    # L4
    tickets_sold_by_trio = andrea_tickets + jude_tickets + sandra_tickets

    # L5
    total_tickets_available = 100 # one hundred tickets to be sold
    tickets_needed_to_be_sold = total_tickets_available - tickets_sold_by_trio

    # FA
    answer = tickets_needed_to_be_sold
    return answer