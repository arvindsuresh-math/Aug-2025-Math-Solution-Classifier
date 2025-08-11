def solve():
    """Index: 3467.
    Returns: the total amount George will receive from his parents.
    """
    # L1
    current_age = 25 # his 25th birthday
    start_age = 15 # Since his 15th birthday
    num_bills_received = current_age - start_age

    # L2
    total_percentage = 100 # WK
    spent_percentage = 20 # spent 20% of his special bills
    remaining_percentage = total_percentage - spent_percentage

    # L3
    remaining_percentage_decimal = 0.8 # He spent 20% of his special bills, so 80% (0.8) are left.
    num_bills_left = num_bills_received * remaining_percentage_decimal

    # L4
    exchange_rate = 1.5 # give him $1.5 in exchange
    total_received = num_bills_left * exchange_rate

    # FA
    answer = total_received
    return answer