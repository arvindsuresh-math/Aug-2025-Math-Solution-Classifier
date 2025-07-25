def solve():
    """Index: 4316.
    Returns: the total money taken by the sky diving company.
    """
    # L1
    individual_bookings = 12000 # individual bookings worth $12,000
    group_bookings = 16000 # group bookings worth $16,000
    total_bookings = individual_bookings + group_bookings

    # L2
    returned_money = 1600 # $1600 has had to be returned to them
    final_total = total_bookings - returned_money

    # FA
    answer = final_total
    return answer