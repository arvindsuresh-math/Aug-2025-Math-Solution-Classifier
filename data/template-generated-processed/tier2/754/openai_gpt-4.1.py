def solve():
    """Index: 754.
    Returns: the final bill Yvette pays including tip.
    """
    # L1
    alicia_sundae = 7.50 # Alicia orders the peanut butter sundae for $7.50
    brant_sundae = 10.00 # Brant orders the Royal banana split sundae for $10.00
    josh_sundae = 8.50 # Josh orders the death by chocolate sundae for $8.50
    yvette_sundae = 9.00 # Yvette orders the cherry jubilee sundae for $9.00
    sundae_total = alicia_sundae + brant_sundae + josh_sundae + yvette_sundae

    # L2
    tip_percent = 0.20 # she leaves her waiter a 20% tip
    tip_amount = sundae_total * tip_percent

    # L3
    final_bill = sundae_total + tip_amount

    # FA
    answer = final_bill
    return answer