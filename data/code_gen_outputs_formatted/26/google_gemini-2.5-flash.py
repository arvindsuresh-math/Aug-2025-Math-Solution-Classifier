def solve(
        seawater_liters: int = 2, # He collects 2 liters of seawater
        salt_percentage: float = 0.20 # the water is 20% salt
    ):
    """Index: 26.
    Returns: the amount of salt in milliliters Jack will get when all the water evaporates.
    """

    #: L1
    liters_of_salt = seawater_liters * salt_percentage

    #: L2
    ml_of_salt = liters_of_salt * 1000

    #: FA
    answer = ml_of_salt
    return answer