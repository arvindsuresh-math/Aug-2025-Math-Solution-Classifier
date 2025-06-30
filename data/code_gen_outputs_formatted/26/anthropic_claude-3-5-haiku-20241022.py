def solve(
    seawater_volume: float = 2,  # Jack collects 2 liters of seawater
    salt_percentage: float = 0.2,  # the water is 20% salt
    ml_per_liter: int = 1000  # conversion from liters to milliliters
):
    """Index: 26.
    Returns: the amount of salt in milliliters after water evaporates."""

    #: L1
    salt_volume_liters = seawater_volume * salt_percentage

    #: L2
    salt_volume_ml = salt_volume_liters * ml_per_liter

    #: FA
    answer = salt_volume_ml
    return answer