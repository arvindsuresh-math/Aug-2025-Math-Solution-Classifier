def solve():
    """Index: 2805.
    Returns: the combined weight in ounces of Puffy and Muffy on the scale.
    """
    # L1
    scruffy_weight = 12 # Scruffy weighs 12 ounces
    muffy_less_than_scruffy = 3 # Muffy weighs 3 ounces less than Scruffy
    muffy_weight = scruffy_weight - muffy_less_than_scruffy

    # L2
    puffy_more_than_muffy = 5 # Puffy weighs 5 ounces more than Muffy
    puffy_weight = puffy_more_than_muffy + muffy_weight

    # L3
    combined_weight = muffy_weight + puffy_weight

    # FA
    answer = combined_weight
    return answer