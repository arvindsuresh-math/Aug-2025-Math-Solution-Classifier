def solve():
    """Index: 716.
    Returns: the total number of cents they have combined.
    """
    # L1
    dollar_in_cents = 100 # WK
    margaret_dollar_fraction = 0.75 # three-fourths of a dollar
    margaret_amount = dollar_in_cents * margaret_dollar_fraction / dollar_in_cents # 100 * 0.75 = $0.75

    # L2
    guy_quarter1 = 0.25 # two quarters
    guy_quarter2 = 0.25 # two quarters
    guy_dime = 0.10 # a dime
    guy_amount = guy_quarter1 + guy_quarter2 + guy_dime

    # L3
    bill_num_dimes = 6 # six dimes
    dime_value = 0.10 # $0.10 per dime
    bill_amount = bill_num_dimes * dime_value

    # L4
    lance_amount = 0.70 # Lance has 70 cents
    total_dollars = lance_amount + margaret_amount + guy_amount + bill_amount

    # L5
    total_cents = total_dollars * dollar_in_cents

    # FA
    answer = int(round(total_cents))
    return answer