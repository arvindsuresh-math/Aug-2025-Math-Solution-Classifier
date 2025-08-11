def solve():
    """Index: 4949.
    Returns: the total amount Françoise will give back to the association.
    """
    # L1
    cost_price_per_pot = 12 # buys them at €12 each
    profit_percentage_value = 25 # sells them at a 25% higher cost
    percentage_divisor = 100 # 25% higher cost
    benefit_per_pot = cost_price_per_pot * profit_percentage_value / percentage_divisor

    # L2
    num_pots_sold = 150 # selling 150 pots of lily of the valley
    total_to_association = num_pots_sold * benefit_per_pot

    # FA
    answer = total_to_association
    return answer