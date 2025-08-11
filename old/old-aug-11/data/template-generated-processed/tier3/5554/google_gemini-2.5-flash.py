def solve():
    """Index: 5554.
    Returns: the total number of cups of flour and eggs used.
    """
    # L1
    eggs_used = 60 # If he uses 60 eggs
    flour_divisor = 2 # half as many cups of flour
    cups_of_flour = eggs_used / flour_divisor

    # L2
    total_ingredients = cups_of_flour + eggs_used

    # FA
    answer = total_ingredients
    return answer