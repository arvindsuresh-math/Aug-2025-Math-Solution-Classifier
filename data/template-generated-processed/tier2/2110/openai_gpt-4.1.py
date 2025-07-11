def solve():
    """Index: 2110.
    Returns: the amount of change Julia receives after her purchase.
    """
    # L1
    snickers_price = 1.5 # each piece of Snickers costs $1.5
    snickers_qty = 2 # 2 pieces of Snickers
    snickers_total = snickers_price * snickers_qty

    # L2
    mms_pack_price = 3 # One pack of M&M's costs $3 (same as 2 Snickers)
    mms_qty = 3 # 3 packs of M&M's
    mms_total = mms_pack_price * mms_qty

    # L3
    total_payment = snickers_total + mms_total

    # L4
    bill_value = 10 # $10 bill
    bill_qty = 2 # 2 $10 bills
    cash_given = bill_value * bill_qty

    # L5
    change = cash_given - total_payment

    # FA
    answer = change
    return answer