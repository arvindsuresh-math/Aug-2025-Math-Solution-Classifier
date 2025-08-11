def solve():
    """Index: 3254.
    Returns: the additional charge per letter for international shipping in cents.
    """
    # L1
    cents_per_dollar = 100 # WK
    standard_postage_dollars = 1.08 # Standard postage is $1.08 per letter
    standard_postage_cents = int(standard_postage_dollars * cents_per_dollar)

    # L2
    num_letters = 4 # four letters
    total_standard_postage_cents = standard_postage_cents * num_letters

    # L3
    total_paid_dollars = 4.60 # paying $4.60
    total_paid_cents = int(total_paid_dollars * cents_per_dollar)
    international_charge_total_cents = total_paid_cents - total_standard_postage_cents

    # L4
    num_international_letters = 2 # two letters internationally
    additional_charge_per_letter_cents = international_charge_total_cents / num_international_letters

    # FA
    answer = additional_charge_per_letter_cents
    return answer