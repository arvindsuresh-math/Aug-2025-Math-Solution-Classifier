def solve(
    seawater_volume: float = 2,  # Jack collects 2 liters of seawater
    salt_percentage: float = 0.2,  # the water is 20% salt
    ml_per_liter: int = 1000  # conversion from liters to milliliters
):
    """Index: 26.
    Returns: the amount of salt in milliliters after water evaporates."""
    #: L1
    salt_volume_liters = seawater_volume * salt_percentage # eval: 0.4 = 2 * 0.2
    #: L2
    salt_volume_ml = salt_volume_liters * ml_per_liter # eval: 400.0 = 0.4 * 1000
    answer = salt_volume_ml  # FINAL ANSWER # eval: 400.0 = 400.0  # FINAL ANSWER
    return answer # eval: return 400.0