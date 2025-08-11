def solve():
    """Index: 5019.
    Returns: the number of suckers Jen ate.
    """
    # L1
    taylor_gave_callie = 5 # gave the last 5 to Callie
    taylor_ate = 1 # Taylor ate one
    taylor_received = taylor_gave_callie + taylor_ate

    # L2
    harmony_kept = 3 # Harmony kept 3
    harmony_received = harmony_kept + taylor_received

    # L3
    molly_ate = 2 # Molly ate 2
    molly_received = harmony_received + molly_ate

    # L4
    multiplier_for_half = 2 # Jen ate half and gave the rest to Molly
    jen_original_had = molly_received * multiplier_for_half

    # L5
    jen_ate = jen_original_had - molly_received

    # FA
    answer = jen_ate
    return answer