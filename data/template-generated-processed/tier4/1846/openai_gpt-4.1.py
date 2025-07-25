def solve():
    """Index: 1846.
    Returns: the total amount Bob and Kate have to pay after discounts.
    """
    # L1
    bob_discount_percent = 5 # 5% for Bob
    percent_divisor = 100 # WK
    bob_bill = 30 # $30 bill to Bob
    bob_discount = (bob_discount_percent / percent_divisor) * bob_bill

    # L2
    bob_final = bob_bill - bob_discount

    # L3
    kate_discount_percent = 2 # 2% for Kate
    kate_bill = 25 # $25 bill to Kate
    kate_discount = (kate_discount_percent / percent_divisor) * kate_bill

    # L4
    kate_final = kate_bill - kate_discount

    # L5
    total_payment = bob_final + kate_final

    # FA
    answer = total_payment
    return answer