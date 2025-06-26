def solve(
        seawater_liters: int = 2, # He collects 2 liters of seawater
        salt_percentage: int = 20, # the water is 20% salt
        ml_per_liter: int = 1000 # 1000 ml/liter (from solution step L2)
    ):
    """Index: 26.
    Returns: the amount of salt in ml.
    """

    #: L1
    liters_of_salt = seawater_liters * (salt_percentage * 0.01)

    #: L2
    ml_of_salt = liters_of_salt * ml_per_liter

    answer = ml_of_salt # FINAL ANSWER
    return answer