def solve(
        volume_seawater_liters: int = 2, # He collects 2 liters of seawater
        salt_percentage: int = 20 # the water is 20% salt
    ):
    """Index: 26.
    Returns: the amount of salt in milliliters Jack will get when all the water evaporates.
    """
    #: L1
    salt_liters = volume_seawater_liters * (salt_percentage / 100)

    #: L2
    salt_ml = salt_liters * 1000

    answer = salt_ml # FINAL ANSWER
    return answer