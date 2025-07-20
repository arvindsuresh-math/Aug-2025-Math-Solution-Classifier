def solve():
    """Index: 3658.
    Returns: the difference in dollars paid between people at the gate and those who pre-bought tickets.
    """
    # L1
    pre_bought_people = 20 # Twenty people pre-bought plane tickets
    pre_bought_price = 155 # $155 per ticket
    total_pre_bought_cost = pre_bought_people * pre_bought_price

    # L2
    gate_bought_people = 30 # Thirty people bought their plane tickets at the gate
    gate_bought_price = 200 # they each paid $200 for their ticket
    total_gate_bought_cost = gate_bought_people * gate_bought_price

    # L3
    difference_in_cost = total_gate_bought_cost - total_pre_bought_cost

    # FA
    answer = difference_in_cost
    return answer