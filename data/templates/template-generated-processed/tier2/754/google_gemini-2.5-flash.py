def solve():
    """Index: 754.
    Returns: the final bill amount.
    """
    # L1
    alicia_sundae_cost = 7.50 # Alicia orders the peanut butter sundae for $7.50
    brant_sundae_cost = 10.00 # Brant orders the Royal banana split sundae for $10.00
    josh_sundae_cost = 8.50 # Josh orders the death by chocolate sundae for $8.50
    yvette_sundae_cost = 9.00 # Yvette orders the cherry jubilee sundae for $9.00
    sundae_total_cost = alicia_sundae_cost + brant_sundae_cost + josh_sundae_cost + yvette_sundae_cost

    # L2
    tip_percent_num = 20 # a 20% tip
    tip_percent_decimal = 0.20 # from solution text: 35*.20
    tip_amount = sundae_total_cost * tip_percent_decimal

    # L3
    final_bill = sundae_total_cost + tip_amount

    # FA
    answer = final_bill
    return answer