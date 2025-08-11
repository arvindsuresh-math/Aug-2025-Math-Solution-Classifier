def solve():
    """Index: 7308.
    Returns: the total number of vacations and classes Grant and Kelvin have.
    """
    # L1
    grant_multiplier = 4 # four times as many vacations
    kelvin_classes = 90 # Kelvin has 90 classes
    grant_vacations = grant_multiplier * kelvin_classes

    # L2
    total_vacations_classes = grant_vacations + kelvin_classes

    # FA
    answer = total_vacations_classes
    return answer