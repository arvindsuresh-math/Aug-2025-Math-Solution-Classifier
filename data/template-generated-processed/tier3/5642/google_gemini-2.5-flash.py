def solve():
    """Index: 5642.
    Returns: the total number of pies they can make.
    """
    # L1
    christine_pounds = 10 # Christine picked 10 pounds of strawberries
    rachel_multiplier = 2 # twice as much as Rachel
    rachel_pounds = christine_pounds * rachel_multiplier

    # L2
    total_pounds = christine_pounds + rachel_pounds

    # L3
    pounds_per_pie = 3 # 3 pounds of strawberries per pie
    num_pies = total_pounds / pounds_per_pie

    # FA
    answer = num_pies
    return answer