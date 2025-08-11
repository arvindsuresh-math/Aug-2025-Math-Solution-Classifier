def solve():
    """Index: 300.
    Returns: the amount of change Jenny should get after her purchase.
    """
    # L1
    num_copies = 7 # 7 copies
    pages_per_copy = 25 # 25-page essay
    total_pages = num_copies * pages_per_copy

    # L2
    cost_per_page = 0.10 # $.10 to print one page
    printing_cost = total_pages * cost_per_page

    # L3
    num_pens = 7 # 7 pens
    cost_per_pen = 1.50 # $1.50 per pen
    pens_cost = num_pens * cost_per_pen

    # L4
    total_spent = printing_cost + pens_cost

    # L5
    num_twenty_bills = 2 # 2 twenty dollar bills
    bill_value = 20 # $20 per bill
    total_paid = num_twenty_bills * bill_value

    # L6
    change = total_paid - total_spent

    # FA
    answer = change
    return answer