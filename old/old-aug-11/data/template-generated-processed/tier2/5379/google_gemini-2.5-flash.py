def solve():
    """Index: 5379.
    Returns: how many more cents Gina needs to tip to be considered a good tipper.
    """
    # L1
    bill_amount_dollars = 26 # bill of $26
    cents_per_dollar = 100 # WK
    bill_amount_cents = bill_amount_dollars * cents_per_dollar

    # L2
    gina_tip_percent_text = 5 # tipped 5%
    gina_tip_percent_calc = 5 # from solution text: 2600*5*.01
    percent_factor = 0.01 # WK
    gina_tip_amount_cents = bill_amount_cents * gina_tip_percent_calc * percent_factor

    # L3
    good_tipper_percent_text = 20 # at least 20%
    good_tipper_percent_calc = 20 # from solution text: 2600*20*.01
    good_tip_amount_cents = bill_amount_cents * good_tipper_percent_calc * percent_factor

    # L4
    additional_tip_needed_cents = good_tip_amount_cents - gina_tip_amount_cents

    # FA
    answer = additional_tip_needed_cents
    return answer