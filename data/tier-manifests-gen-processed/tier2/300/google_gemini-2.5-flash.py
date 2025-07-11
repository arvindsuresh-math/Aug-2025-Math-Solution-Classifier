def solve():
    """Index: 300.
    Returns: the amount of money Jenny should get in change.
    """
    # L1
    num_copies = 7 # print 7 copies
    pages_per_essay = 25 # 25-page essay
    total_pages_to_print = num_copies * pages_per_essay

    # L2
    cost_per_page_decimal = 0.10 # $.10 to print one page
    printing_cost = total_pages_to_print * cost_per_page_decimal

    # L3
    num_pens = 7 # buy 7 pens
    cost_per_pen = 1.50 # each cost $1.50
    pens_cost = num_pens * cost_per_pen

    # L4
    total_spend = printing_cost + pens_cost

    # L5
    num_twenty_dollar_bills = 2 # 2 twenty dollar bills
    twenty_dollar_bill_value = 20 # 2 twenty dollar bills
    amount_paid = num_twenty_dollar_bills * twenty_dollar_bill_value

    # L6
    change_amount = amount_paid - total_spend

    # FA
    answer = change_amount
    return answer