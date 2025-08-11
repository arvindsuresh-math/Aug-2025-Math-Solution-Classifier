def solve():
    """Index: 5921.
    Returns: the total cost in dollars Freddy spent calling his family.
    """
    # L1
    local_call_cost_per_minute = 5 # Local calls cost 5 cents a minute
    local_call_duration = 45 # talk for 45 minutes
    cost_local_call_cents = local_call_cost_per_minute * local_call_duration

    # L2
    international_call_cost_per_minute = 25 # international calls cost 25 cents a minute
    international_call_duration = 31 # talk for 31 minutes
    cost_international_call_cents = international_call_cost_per_minute * international_call_duration

    # L3
    total_cost_cents = cost_local_call_cents + cost_international_call_cents

    # L4
    cents_per_dollar = 100 # Since each dollar has 100 cents
    total_cost_dollars = total_cost_cents / cents_per_dollar

    # FA
    answer = total_cost_dollars
    return answer