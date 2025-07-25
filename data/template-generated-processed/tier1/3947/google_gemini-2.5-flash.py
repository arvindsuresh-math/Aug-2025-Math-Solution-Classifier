def solve():
    """Index: 3947.
    Returns: the combined number of nuts Bill and Harry have.
    """
    # L1
    sue_nuts = 48 # Sue has 48 nuts
    harry_multiplier_sue = 2 # twice as many nuts as Sue
    harry_nuts = harry_multiplier_sue * sue_nuts

    # L2
    bill_multiplier_harry = 6 # 6 times as many nuts as Harry
    bill_nuts = harry_nuts * bill_multiplier_harry

    # L3
    combined_nuts = bill_nuts + harry_nuts

    # FA
    answer = combined_nuts
    return answer