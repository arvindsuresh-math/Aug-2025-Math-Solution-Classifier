def solve():
    """Index: 1086.
    Returns: the number of kilograms of tomatoes that are not sold.
    """
    # L1
    sold_to_maxwell = 125.5 # sold 125.5 kg to Mrs. Maxwell
    sold_to_wilson = 78 # sold 78 kg to Mr. Wilson
    total_sold = sold_to_maxwell + sold_to_wilson

    # L2
    total_harvested = 245.5 # harvested 245.5 kg of tomatoes
    unsold = total_harvested - total_sold

    # FA
    answer = unsold
    return answer