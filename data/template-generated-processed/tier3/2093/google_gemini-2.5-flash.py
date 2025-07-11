def solve():
    """Index: 2093.
    Returns: Jan's height.
    """
    # L1
    cary_height = 72 # Cary is 72 inches tall
    half_divisor = 2 # half her height
    bill_height = cary_height / half_divisor

    # L2
    jan_taller_amount = 6 # Jan is 6 inches taller than Bill
    jan_height = bill_height + jan_taller_amount

    # FA
    answer = jan_height
    return answer