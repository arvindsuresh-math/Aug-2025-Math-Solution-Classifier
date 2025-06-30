def solve(
    liters_seawater: float = 2.0, # He collects 2 liters of seawater
    salt_percentage: float = 0.20 # the water is 20% salt
):
    """Index: 26.
    Returns: the number of ml of salt Jack will get when all the water evaporates.
    """
    #: L1
    liters_salt = liters_seawater * salt_percentage

    #: L2
    ml_salt = liters_salt * 1000 # There are 1000 ml in a liter

    answer = ml_salt # FINAL ANSWER
    return answer