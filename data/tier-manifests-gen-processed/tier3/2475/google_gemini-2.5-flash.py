def solve():
    """Index: 2475.
    Returns: the amount of money Julie gave Sarah in cents.
    """
    # L1
    total_dollars = 3 # 3 dollars
    cents_per_dollar = 100 # one dollar is 100 cents
    total_cents = total_dollars * cents_per_dollar

    # L2
    total_lollipops = 12 # 12 lollipops
    cost_per_lollipop = total_cents / total_lollipops

    # L3
    share_denominator = 4 # one-quarter of the lollipops
    lollipops_shared = total_lollipops / share_denominator

    # L4
    reimbursement_amount = lollipops_shared * cost_per_lollipop

    # FA
    answer = reimbursement_amount
    return answer