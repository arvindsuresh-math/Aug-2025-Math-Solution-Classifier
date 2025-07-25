def solve(
        seawater_liters: int = 2, # He collects 2 liters of seawater
        salt_percentage: int = 20, # the water is 20% salt
        ml_per_liter: int = 1000 # 1000 ml/liter (from solution step L2)
    ):
    """Index: 26.
    Returns: the amount of salt in ml.
    """

    #: L1
    liters_of_salt = 1.4 # eval: 1.4 = 1.4

    #: L2
    ml_of_salt = liters_of_salt * ml_per_liter # eval: 1400.0 = 1.4 * 1000

    #: FA
    answer = ml_of_salt
    return answer # eval: return 1400.0
