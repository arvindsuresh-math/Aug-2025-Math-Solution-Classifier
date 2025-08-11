def solve():
    """Index: 6966.
    Returns: the amount of dollars Darnell would pay less on the alternative plan.
    """
    # L1
    texts_sent = 60 # Darnell sends 60 texts
    texts_per_dollar = 30 # $1 per 30 texts
    texting_charge_multiplier = texts_sent / texts_per_dollar

    # L2
    minutes_spent = 60 # spends 60 minutes on the phone
    minutes_per_three_dollars = 20 # $3 per 20 minutes of calls
    call_charge_multiplier = minutes_spent / minutes_per_three_dollars

    # L3
    cost_per_30_texts = 1 # $1 per 30 texts
    cost_per_20_minutes = 3 # $3 per 20 minutes of calls
    texting_cost_subtotal = texting_charge_multiplier * cost_per_30_texts
    calling_cost_subtotal = call_charge_multiplier * cost_per_20_minutes
    alternative_plan_cost = texting_cost_subtotal + calling_cost_subtotal

    # L4
    current_plan_cost = 12 # $12 for unlimited texting and calling
    savings = current_plan_cost - alternative_plan_cost

    # FA
    answer = savings
    return answer