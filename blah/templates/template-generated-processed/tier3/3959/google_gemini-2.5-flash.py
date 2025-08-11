def solve():
    """Index: 3959.
    Returns: the total amount Annie will pay for 12 kg of oranges.
    """
    # L1
    price_paid_initial = 6 # Annie paid $6
    mass_purchased_initial = 2 # for 2 kg of oranges
    price_per_kg = price_paid_initial / mass_purchased_initial

    # L2
    mass_purchased_final = 12 # for 12 kg of oranges
    total_cost_final = mass_purchased_final * price_per_kg

    # FA
    answer = total_cost_final
    return answer