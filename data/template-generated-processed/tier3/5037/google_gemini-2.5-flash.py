from fractions import Fraction

def solve():
    """Index: 5037.
    Returns: the total number of watches Julia owns after the purchase.
    """
    # L1
    silver_watches = 20 # 20 silver watches
    bronze_multiplier = 3 # three times as many bronze watches
    bronze_watches = bronze_multiplier * silver_watches

    # L2
    total_silver_bronze_watches = bronze_watches + silver_watches

    # L3
    gold_percentage = Fraction(10, 100) # 10% of all the watches she owns
    gold_watches = total_silver_bronze_watches * gold_percentage

    # L4
    total_watches = silver_watches + bronze_watches + gold_watches

    # FA
    answer = total_watches
    return answer